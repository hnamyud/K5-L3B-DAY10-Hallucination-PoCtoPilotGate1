"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Cổng S6 (Vòng 2): Nếu đơn có nhiều kiện cùng trễ mà ticket không chỉ rõ parcel_id -> chuyển người xử lý
    order_id = ctx.ticket.get("order_id")
    order = ctx.tools.lookup_order(order_id) if order_id else None
    if order:
        delayed = [p for p in order.get("parcels", []) if H.db_delay_days(p, ctx.as_of) > 0]
        if len(delayed) > 1 and not ctx.ticket.get("parcel_id"):
            ctx.log("escalate_ambiguous_parcels", order_id=order_id, delayed_count=len(delayed))
            return Verdict.escalate("đơn có nhiều kiện trễ nhưng không rõ kiện nào, chuyển người xử lý")

    # Cổng 1: Ghim đúng phiên bản chính sách đang có hiệu lực theo ngày hệ thống (as_of)
    policies = ctx.tools.lookup_policies()
    eff = H.effective_policy(policies, ctx.as_of)
    if eff:
        ctx.log("pin_policy", policy_id=eff["policy_id"])
        return Verdict.allow(policy_id=eff["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    order_id = action.get("order_id")
    order = ctx.tools.lookup_order(order_id) if order_id else None
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)

    if tool == "issue_refund" and order and policy:
        # Cổng 2a: Chặn hoàn tiền trùng (kiểm tra sổ cái thời gian thực)
        if ctx.tools.ledger_rows(order_id=order_id):
            ctx.log("block_duplicate_refund", order_id=order_id)
            return Verdict.deny("đơn đã được hoàn tiền trong sổ cái")

        # Cổng 2b: Đối chiếu số tiền hoàn với tracking DB & chính sách hiệu lực (chặn model_override / fail_open)
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        db_delay = H.db_delay_days(parcel, ctx.as_of)
        expected = H.entitlement_vnd(policy, order, db_delay, parcel.get("delay_cause"))
        if action.get("amount_vnd", 0) > expected:
            ctx.log("block_over_refund", asked=action.get("amount_vnd"), expected=expected, db_delay=db_delay)
            return Verdict.deny("số tiền hoàn vượt mức hợp lệ theo tracking DB")

    if tool == "file_carrier_fault" and order and policy:
        # Cổng 3: Chặn ghi lỗi oan cho hãng nếu tracking DB không thỏa điều kiện phạt
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        db_delay = H.db_delay_days(parcel, ctx.as_of)
        if not H.carrier_at_fault(policy, parcel, db_delay):
            ctx.log("block_wrongful_fault", parcel_id=parcel.get("parcel_id"), db_delay=db_delay)
            return Verdict.deny("không đủ điều kiện ghi lỗi hãng theo tracking DB")
        # Cổng S6b (Vòng 2): Chặn ghi quá trần số lỗi tự động/hãng/ngày (từ lỗi thứ 3 trở đi)
        strike_cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        target_carrier = parcel["carrier_id"]
        if strike_cap is not None and len(ctx.tools.fault_rows(carrier_id=target_carrier)) >= strike_cap:
            ctx.log("block_carrier_strike_cap", carrier_id=target_carrier, limit=strike_cap)
            return Verdict.deny("vượt trần số lỗi tự động của hãng trong ngày")
        # Cổng S6 (Vòng 2): Sửa đúng kiện, hãng và tài xế thực sự trễ thay vì mặc định parcels[0]
        if action.get("parcel_id") != parcel["parcel_id"] or action.get("carrier_id") != target_carrier:
            ctx.log("fix_fault_parcel", old_parcel=action.get("parcel_id"), new_parcel=parcel["parcel_id"],
                    carrier_id=target_carrier)
            return Verdict.modify(
                "chuyển lỗi về đúng kiện và hãng trễ theo tracking DB",
                parcel_id=parcel["parcel_id"],
                carrier_id=target_carrier,
                driver_id=parcel.get("driver_id"),
            )

    return Verdict.allow()
