# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** `K5-L3B-DAY10-Hallucination-PoCtoPilotGate1` · **Thẻ đã bốc:** S6 *(để trống tới phút 125; bốc số xong thì ghi đúng số đó, ví dụ `S3`. Lab Coach đối chiếu với sổ; lệnh tự kiểm tra in dòng này trong report.)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | `R-S6-prepared-20261119-165101-b504cd` | S6 · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | 0.3333 | 0.3333 | 270000đ · 25 · 0 | 0.0 | Cổng vòng 1 giảm lỗi hãng oan từ 40 xuống 25, nhưng chưa xử lý được đơn tách kiện nên vẫn hỏng `S6-01`, `S6-02`. |
| 2 | `R-S6-after-20261119-170331-b58785` | S6 · after | Thêm cổng S6 trong `guards.py` (escalate đơn nhiều kiện trễ mơ hồ; modify đúng kiện/hãng trễ; deny vượt trần lỗi/hãng/ngày) | 1.0 | 1.0 | 0đ · 0 · 0 | 0.1667 | Xử lý sạch 100% gói sự cố S6 (`wrongful_refund_vnd = 0`, `wrongful_carrier_faults = 0`). |
| 3 | `R-S6-after-20261119-170901-005ba4` | S6 · after | Thêm monitor `multi_parcel_guard_rate` trong `lab10/monitors.py` | 1.0 | 1.0 | 0đ · 0 · 0 | 0.1667 | Monitor sáng đèn trên S6 (`0.0 -> 0.666667`), mọi chỉ số đạt 100%. |
| 4 | `R-S6-grade-20261119-173059-005ba4` | base · after | (kiểm không regression sau khi sửa S6) | 1.0 | 1.0 | 0đ · 0 · 0 | 0.2273 | Không có ca mới hỏng trên bộ nền (`0.9909 -> 1.0`). |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S6-grade-20261119-165100-b504cd` · base: `R-S6-before-20261119-165101-b504cd` · prepared: `R-S6-prepared-20261119-165101-b504cd`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): Giảm `wrongful_carrier_faults` từ `40` xuống `25` (`-15` lỗi oan).
- Khối kinh doanh và vận hành còn dòng nào vượt trần: Không vượt trần kinh doanh/vận hành, nhưng `pass_rate` (`0.3333`), `pass_k` (`0.3333`), `wrongful_refund_vnd` (`270000đ`) và `wrongful_carrier_faults` (`25`) đều chưa đạt ngưỡng đã ký.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? **Kỹ thuật** (chọn nhầm kiện `parcels[0]`) và **Pháp lý** (ghi lỗi oan cho bên thứ ba).
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? **Chưa nằm trong pre-mortem vòng 1** (vòng 1 mới tập trung vào lệch ngày trễ và hoàn trùng ở đơn 1 kiện, chưa xét đơn tách nhiều kiện giao bởi nhiều hãng).
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| Đơn tách nhiều kiện bị lấy nhầm `parcels[0]` để ghi lỗi hãng, khiến hãng giao đúng hẹn bị trừ thưởng oan. | Kỹ thuật / Pháp lý | `tracking.parcels` và `file_carrier_fault` trên trace |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `hãng vận chuyển giao đúng hẹn (Sông Hồng / GHSH / DNB)` · đo bằng gì `wrongful_carrier_faults` · bao nhiêu ở mốc base `40`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S6-01@11`: `06 tool file_carrier_fault` ghi lỗi cho `O-2601-P1` (`GHSH`, `delay: 0`), trong khi `02 tracking` ghi `O-2601-P2` (`VNX`, `delay: 4`) mới là kiện trễ. | Hãng `GHSH` bị ghi lỗi oan dù giao đúng hẹn. | Cao | Lỗi chìm |
| 2 | `S6-20@11`: Đơn `O-2620` có 2 kiện cùng trễ (`GHSH: 3`, `VNX: 5`) và ticket thiếu `parcel_id`, nhưng agent vẫn tự hoàn `26.000đ` và ghi lỗi `GHSH` (nhãn đúng: `escalated`). | Hãng `GHSH` và ngân quỹ LogiX (`26.000đ`). | Cao | Lỗi chìm |
| 3 | `S6-42@11`: `07 tool file_carrier_fault` tiếp tục ghi lỗi tự động thứ 3 trong ngày cho `GHSH` (`O-2642-P1`), vượt trần 2 lỗi/ngày (nhãn đúng: `faults: []`). | Hãng nhỏ `GHSH` bị dồn lỗi tự động vượt trần. | Cao | Lỗi chìm |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | Không | **Có** (tự suy diễn kiện trễ khi khách không nêu `parcel_id`) | Không |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | Không | **Có** (ticket thiếu `parcel_id` để phân biệt 2 kiện cùng trễ) | Không |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | **Có** (agent lấy `parcels[0]` cấp đơn thay vì kiện thực sự trễ ở tracking) | Không | **Có** (ghi sổ lỗi nhưng không đối chiếu `fault_rows` với trần `ops_limits`) |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | Không | Không | Không |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | Hãng `GHSH` giao đúng hẹn (`delay = 0`) nhưng bị trừ thưởng vì kiện của hãng khác (`VNX`). | Không có bằng chứng rõ kiện nào bị khiếu nại nhưng vẫn tự động hoàn tiền và phạt hãng. | Hãng `GHSH` bị ghi quá 2 lỗi tự động/ngày mà không qua người duyệt. |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Khác: `write_gate` dùng `Verdict.modify` sửa đúng `parcel_id`, `carrier_id`, `driver_id` theo tracking DB. | Trao quyền kiểm soát cho người: `pre_guard` trả `Verdict.escalate` khi có > 1 kiện trễ và thiếu `parcel_id`. | Khác: `write_gate` dùng `Verdict.deny` chặn ghi lỗi tự động khi đạt trần `max_auto_strikes_per_carrier_per_day`. |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | Lỗi được chuyển đúng sang `VNX` (`O-2601-P2`); `GHSH` không bị ghi oan. | Ticket chuyển hàng chờ CSKH → nhân viên xác minh kiện với khách → duyệt/từ chối và trả lời. | Khách vẫn được hoàn tiền theo chính sách; lỗi hãng vượt trần để người đối soát xử lý sau. |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | `multi_parcel_guard_rate` (theo dõi `fix_fault_parcel`). | `multi_parcel_guard_rate` (theo dõi `escalate_ambiguous_parcels`). | `multi_parcel_guard_rate` (theo dõi `block_carrier_strike_cap`). |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `điều phối` | Nhóm B: `kế toán đối soát` |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | Điều phối nhận thông báo ghi lỗi và rà các ca ảnh hưởng đến tài xế. Thẻ S6 ghi nhận trưởng nhóm tài xế Sông Hồng phản ánh bị trừ thưởng. | Chị Oanh so các khoản hoàn và bản ghi lỗi liên quan khi khớp sổ với hãng và shop hằng tuần. |
| Mục tiêu chính của họ | Quy trách nhiệm đúng kiện, hãng và tài xế dựa trên hành trình thực tế, tránh đưa lỗi oan vào bảng thưởng. | Đối soát được khoản ghi nhận với đúng đơn, kiện, đối tác và căn cứ để xác định lệch sổ hoặc khoản cần điều chỉnh. |
| Hiện nay họ xác định “ai chịu lỗi giao trễ” theo các bước nào | (1) Lấy mã đơn và mã kiện từ thông báo. (2) Đối chiếu mốc hẹn, mốc giao, hãng và tài xế của từng kiện. (3) Nếu thông báo trỏ sai kiện hoặc chưa đủ căn cứ, yêu cầu LogiX xác minh trước khi dùng bản ghi để tính thưởng. | (1) Ghép ticket và khoản hoàn theo mã đơn. (2) Nối bản ghi lỗi sang đúng mã kiện, hãng và tracking, đối chiếu chính sách có hiệu lực. (3) Đưa khoản thiếu căn cứ hoặc lệch sang đối soát với hãng trước khi chốt sổ. |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | Thẻ chỉ có phản ánh từ Sông Hồng. Cần xác nhận hãng khác có cùng cách lưu tracking và rà thưởng hay không. | Phiếu A nêu nhịp đối soát hằng tuần. Chưa có bằng chứng về biểu mẫu hay cách xử lý ngoại lệ của từng hãng/shop. |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì? | Kiện và chặng hãng/tài xế phụ trách. Cùng một đơn có thể có kiện đúng hẹn và kiện trễ do hãng khác chở. | Đơn là khóa nối khoản hoàn với sổ. Trách nhiệm giao trễ phải đối chiếu ở bản ghi lỗi theo kiện và hãng. |


**Hệ thống đang mang hình dung nào?**


- Lệnh ghi lấy kiện đầu làm đại diện cho cả đơn, dù độ trễ đề xuất lấy từ kiện khác. Trace `S6-04@11` mốc `prepared`, dòng `03 tracking` cho thấy `O-2604-P1/GHSH` trễ 1 ngày và `O-2604-P2/VNX` trễ 5 ngày. Dòng `07 tool file_carrier_fault` ghi 5 ngày cho `O-2604-P1/GHSH`, tài xế `TX-GHSH-02`. Dòng 09 gửi thông báo cho GHSH.
- Với điều phối, phải xác định kiện/chặng trước rồi mới gán hãng và tài xế. Với kế toán, dùng mã đơn để nối sổ vẫn phải kiểm căn cứ trên đúng kiện. Lệnh ghi đã ghép độ trễ của kiện này với người chịu lỗi của kiện kia.
- `S6-20@11` không có `parcel_id`; tracking có hai kiện trễ 3 và 5 ngày. Hệ thống đã hoàn 26.000đ rồi ghi lỗi cho kiện đầu GHSH với độ trễ 5 ngày. Nhãn yêu cầu chuyển người, hoàn 0đ và không ghi lỗi. Khi chưa xác định được kiện, chuyển Hạnh/CSKH xác minh **trước `issue_refund`** và chờ đủ căn cứ mới ghi lỗi hoặc thông báo hãng.


### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `file_carrier_fault`


| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `parcel_id`, `carrier_id`, `driver_id`, `delay_days` | WRONG | `S6-04@11`: lệnh ghi lấy độ trễ 5 ngày của `O-2604-P2/VNX` gắn cho `O-2604-P1/GHSH`, kiện chỉ trễ 1 ngày. | GHSH và tài xế `TX-GHSH-02` bị gán lỗi của kiện khác. | Cổng vòng 1 kiểm điều kiện từ kiện tra cứu, cổng pháp lý kiểm nguyên nhân của kiện trong lệnh ghi. Trace cho thấy cả hai vẫn để lệnh này lọt. | **Chặn trước ghi:** đối chiếu toàn bộ bộ khóa và độ trễ với cùng kiện được xác minh. Chỉ ghi cho kiện khớp tracking và chính sách. |
| `ticket.parcel_id` và danh sách `tracking.parcels` | INCOMPLETE | `S6-20@11`: thiếu mã kiện, hai kiện trễ 3 và 5 ngày. Agent tự chọn căn cứ tính tiền và ghi lỗi cho kiện đầu. | LogiX hoàn sai 26.000đ trong trial này và GHSH nhận lỗi thiếu căn cứ. | Chưa có chốt chuyển người khi nhiều kiện cùng trễ mà ticket thiếu mã kiện. | **Chặn trước thao tác ghi đầu tiên:** chuyển Hạnh xác minh kiện trước khi hoàn, ghi lỗi hoặc gửi hãng. |
| Tổng lỗi tự động của cùng `carrier_id` trong ngày | WRONG | Loạt `S6-40` đến `S6-43` cùng scenario `S6-LOAT`. Trace `prepared` seed 11 có 4 bản ghi cho GHSH. `S6-42` và `S6-43` vượt giới hạn 2 lỗi tự động/hãng/ngày trong `ops_limits`. | Lỗi dồn vào cùng hãng trong một ngày, làm tăng nguy cơ ảnh hưởng sai đến tiền phạt hoặc thưởng tài xế. | Trần có trong dữ liệu, lần chạy vẫn ghi cả bốn. | **Giới hạn thiệt hại:** đếm lỗi của cùng hãng trong ngày từ sổ, chuyển duyệt trước lỗi thứ ba. Tách quyết định hoàn tiền hợp lệ khỏi quyết định quy lỗi. |
| Thời điểm cập nhật tracking của từng kiện | INVALID | **Giả thuyết chưa thấy trên trace:** cấu trúc nhiều kiện như `S6-04`, nhưng `delivered_date` hoặc `delay_cause` của kiện vừa được hãng nhập bù sau khi trợ lý đọc. Cần thử lại với dữ liệu cập nhật muộn. | Hãng hoặc tài xế của đúng kiện vẫn có thể bị quy lỗi theo dữ liệu cũ. | Cổng hiện tại đọc nguyên nhân đã ghi; chưa có bằng chứng kiểm tra độ mới hoặc lịch sử sửa của dữ kiện. | **Phát hiện và chuyển duyệt:** nếu mốc tracking còn tranh chấp hoặc có cập nhật sau ảnh chụp dùng để đề xuất, yêu cầu kiểm lại trước khi ghi. |

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: Với mọi lệnh `file_carrier_fault`, `parcel_id` và `carrier_id` được ghi lỗi phải khớp với kiện thực sự trễ theo tracking DB (`H.ticket_parcel`), đồng thời không vượt quá trần lỗi tự động/ngày của hãng (`max_auto_strikes_per_carrier_per_day = 2`); nếu có nhiều hơn 1 kiện trễ mà ticket không nêu `parcel_id` thì phải chuyển người duyệt (`escalated`).

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): Kiểm bằng `pre_guard(ctx)` và `write_gate(ctx, action)` (nhánh `file_carrier_fault`) trong `lab10/guards.py`, và kiểm trên dòng `wrongful_carrier_faults = 0` trong report `lab10.grade --incident S6`.

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): Trong vận hành đơn tách kiện, kiện đứng đầu danh sách là kiện đại diện cho khiếu nại giao trễ của khách.

Vì sao có thể sai: Các hãng vận chuyển từng kiện độc lập, còn khách có thể chỉ nêu mã đơn và nói “giao chậm”. Thẻ S6 ghi nhận kiện Sông Hồng có thể đến đúng hẹn trong khi kiện của hãng khác đến muộn. `S6-20` còn có hai kiện thuộc hai hãng đều trễ và khách không chỉ rõ kiện nào, nên thứ tự kiện không xác định được ai chịu trách nhiệm.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `R-S6-prepared-20261119-165101-b504cd`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: Hãng vận chuyển giao đúng hẹn bị ghi lỗi oan hoặc dồn lỗi vượt trần (cho ai: Hãng Sông Hồng / GHSH / DNB, đo bằng: wrongful_carrier_faults = 25 ở prepared)
 └─ HOẶC
 ├─ [1] Agent ghi lỗi cho `parcels[0]` dù kiện đó giao đúng hẹn (tầng: hành động / data)
 │ └─ vì: `agent.py` mặc định lấy `parcels[0]` thay vì kiện thực sự trễ (bằng chứng: `S6-01@11`, `O-2601-P1` delay 0)
 ├─ [2] Agent tự động hoàn tiền và ghi lỗi hãng khi đơn có nhiều kiện cùng trễ mà thiếu `parcel_id` (tầng: đầu vào)
 │ └─ vì: ticket không nêu rõ kiện nào trễ nhưng không chuyển người duyệt (bằng chứng: `S6-20@11`, `O-2620`)
 └─ [3] Hệ thống ghi lỗi tự động thứ 3 trong ngày cho cùng một hãng (tầng: quyền hạn / vận hành)
 └─ vì: không đối chiếu `fault_rows(carrier_id)` với `max_auto_strikes_per_carrier_per_day = 2` (bằng chứng: `S6-42@11`, `ops_limits`)
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | Lệnh `file_carrier_fault` phải trỏ đúng `parcel_id` và `carrier_id` của kiện thực sự trễ theo tracking DB. | Người thiết kế ngầm tin mỗi đơn chỉ có 1 kiện hoặc kiện đầu tiên (`parcels[0]`) luôn là kiện trễ. |
| [2] | Khi có > 1 kiện cùng trễ mà ticket không nêu `parcel_id`, phải chuyển người duyệt (`escalated`). | Người thiết kế ngầm tin khách hàng luôn ghi rõ mã kiện khi khiếu nại đơn tách kiện. |
| [3] | Không ghi lỗi tự động cho cùng một hãng vượt quá `max_auto_strikes_per_carrier_per_day` (2 lỗi/ngày). | Người thiết kế ngầm tin tần suất lỗi của một hãng trong ngày ít khi chạm trần hoặc có người kiểm lại kịp. |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | Agent mặc định chọn `parcels[0]` khi gọi `file_carrier_fault` dù kiện đó giao đúng hẹn | `write_gate` khi `tool == "file_carrier_fault"` trong `lab10/guards.py`: đối chiếu `H.ticket_parcel(...)` và dùng `Verdict.modify` sửa lại `parcel_id`, `carrier_id`, `driver_id` | Chặn / sửa trước khi ghi | **Ngăn hẳn** (trong phạm vi hệ thống có dữ liệu tracking đúng), vì mọi lệnh ghi đều bị ép trỏ đúng vào kiện trễ trước khi ghi sổ lỗi | `R-S6-after-20261119-170331-b58785` |
| [2] | Đơn có nhiều kiện cùng trễ nhưng ticket không ghi `parcel_id`, dễ quy nhầm hãng | `pre_guard(ctx)` trong `lab10/guards.py`: đếm số kiện trễ > 1 và thiếu `parcel_id` thì trả về `Verdict.escalate` | Chặn trước khi LLM đọc ticket | **Ngăn hẳn** việc tự động hoàn/ghi lỗi nhầm ở các ca mơ hồ, vì chuyển thẳng cho người duyệt xác minh | `R-S6-after-20261119-170331-b58785` |
| [3] | Một hãng bị ghi quá trần số lỗi tự động trong ngày (`max_auto_strikes_per_carrier_per_day = 2`) | `write_gate` khi `tool == "file_carrier_fault"` trong `lab10/guards.py`: kiểm tra `fault_rows(carrier_id)` >= trần thì `Verdict.deny` | Giới hạn thiệt hại | **Ngăn hẳn** việc vượt trần lỗi tự động/ngày cho từng hãng theo `ops_limits()` | `R-S6-after-20261119-170331-b58785` |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `multi_parcel_guard_rate` |
| **Bước / hành vi được đo** | Tần suất cổng bảo vệ phải can thiệp vào đơn tách nhiều kiện hoặc chạm trần lỗi hãng/ngày (`fix_fault_parcel`, `escalate_ambiguous_parcels`, `block_carrier_strike_cap`). |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ (0–1) số lần chạy có ít nhất một sự kiện `guard` thuộc nhóm xử lý đơn tách kiện hoặc trần lỗi hãng/ngày. |
| **Dữ liệu** (trường nào của trial, không có nhãn) | Trường `events` của mỗi `trial` (không cần nhãn đúng/sai), lọc các event có `type == "guard"` và `kind` nằm trong `{"fix_fault_parcel", "escalate_ambiguous_parcels", "block_carrier_strike_cap"}`. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `Số trial có ít nhất 1 event guard thuộc 3 loại trên / max(1, tổng số trial)`. Nếu `events` trống hoặc thiếu thì coi như `0` (không kích hoạt). |
| **Khung thời gian / ngưỡng báo động** | Cửa sổ trượt 24 giờ; báo động khi tỉ lệ vượt `0.20` (20%) để kiểm tra xem có đợt đơn tách kiện bất thường hoặc hãng bị dồn lỗi hàng loạt hay không. |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không thấy lỗi ở những đơn chỉ có 1 kiện nhưng bản thân dữ liệu tracking bị ghi sai hãng từ đầu. |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | Bộ nền: `0.0` · Trên thẻ S6 (`after`): `0.666667` |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `R-S6-after-20261119-165101-b504cd`)


**Trạng thái theo log đính kèm:** Mốc `after` vẫn có 25 lỗi hãng oan, 270.000đ hoàn sai cộng qua các lần thử và `pass_rate = pass_k = 0,3333`, bằng `prepared`. Mốc `base` có 40 lỗi hãng oan. Trong lần này, cổng vòng 1 đã giảm số lỗi oan nhưng chưa xử lý hết sự cố. Log còn báo `integrity`, `visible` và `monitor` không đạt. Các gate đề xuất trong bảng cần được kiểm lại ở mốc `after` sau khi nhóm sửa.


```text
[ĐỈNH] Hãng/tài xế chịu lỗi giao trễ oan, có thể ảnh hưởng thưởng theo phản ánh trên thẻ.
      Chỉ báo trong lab: số bản ghi lỗi hãng oan.
└─ HOẶC
   ├─ [1] Lệnh ghi dùng sai kiện/hãng/tài xế VÀ cổng hiện có vẫn cho qua
   │      S6-04@11: lấy 5 ngày của P2/VNX và ghi vào P1/GHSH.
   ├─ [2] Thiếu mã kiện, nhiều kiện cùng trễ VÀ chưa có chốt chuyển duyệt trước khi hoàn/ghi
   │      S6-20@11: hoàn 26.000đ rồi ghi lỗi GHSH dù kiện khiếu nại chưa được xác minh.
   └─ [3] Lỗi vượt trần trong ngày VÀ chưa chuyển duyệt trước lần ghi tiếp theo
          S6-40 đến S6-43: cùng ngày giả lập, GHSH nhận 4 bản ghi ở seed 11.


```


| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | Hiện có `write_gate` vòng 1 và `legal.carrier_fault_requires_recorded_cause`. Đề xuất thêm đối chiếu cùng một kiện trong `write_gate`. | Chặn | Cổng hiện có giảm lỗi thiếu căn cứ. `S6-01@11` chặn ghi P1 có nguyên nhân trống, nhưng cũng bỏ sót lỗi hợp lệ của P2. `S6-04@11` vẫn lọt. Đối chiếu toàn bộ bộ khóa có thể ngăn ghi lệch kiện nếu tracking đúng và mọi lệnh ghi đều qua cổng. | Chưa có bằng chứng bản sửa đối chiếu cùng kiện đã đạt. Tracking có thể sai hoặc cập nhật muộn. |
| [2] | Đề xuất `pre_guard` chuyển người khi không xác định được kiện trong đơn có nhiều kiện cùng trễ. | Chặn trước ghi và chuyển duyệt | Có thể ngăn quyết định tự động ở ca mơ hồ nếu chuyển trước `issue_refund`. Mốc `after` trong log vẫn có tỷ lệ chuyển người 0% trên S6. | Chờ kiểm ca mơ hồ không phát sinh khoản hoàn hoặc lỗi hãng trước khi duyệt. Cần đo tải hàng chờ sau khi chuyển người. |
| [3] | Đề xuất `write_gate` đối chiếu số lỗi hãng trong ngày từ sổ với `ops_limits.max_auto_strikes_per_carrier_per_day = 2`. | Giới hạn thiệt hại | Có thể ngăn lần ghi tự động thứ ba nếu đếm đúng hãng, đúng ngày, từ trạng thái sổ mới nhất. Hai lượt đầu vẫn cần đúng căn cứ. | Chờ thử liên tiếp trên cùng ngày giả lập và kiểm việc chuyển duyệt. Cần xác minh tính nhất quán của sổ khi có nhiều tiến trình ghi. |




---


<a id="c10"></a>


## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)


| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Ghi lỗi nhầm kiện/hãng/tài xế, hoặc dồn lỗi lên một hãng trong cùng ngày. | Đã xảy ra trong bộ thử S6. Tần suất ngoài thực tế chưa đo. | Cao. Hãng phải đối soát lại, tài xế có thể bị ảnh hưởng thưởng theo phản ánh S6. | Lê Thanh Tùng (NV-TUNG) | `wrongful_carrier_faults > 0` trong report. Mốc `after` còn 25, trong đó phân khúc GHSH có 20. | Tạm tắt ghi lỗi và gửi hãng theo runbook, đối chiếu các bản ghi theo kiện/hãng/tài xế. Kiểm lại ca sai kiện, ca mơ hồ và loạt cùng ngày sau khi bổ sung cổng. | Không đủ căn cứ chọn Tiếp tục khi còn lỗi oan. Chỉ đề nghị mở lại luồng sau khi lần kiểm tra hợp lệ đạt ngưỡng đã ký và ca hợp lệ vẫn qua. | MANAGE |




Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.


---


<a id="c11"></a>


## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5


### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)


Bằng chứng tự kiểm tra của bàn: `R-S6-grade-20261119-165100-b504cd`, đối chiếu với lần tái hiện `prepared` ở C3.2. Trạng thái áp dụng cho mức sẵn sàng sau sự cố.


| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 1 · Chất lượng | Chưa | `visible` chưa đạt. `pass_rate = pass_k = 0,3333`, còn 270.000đ hoàn sai và 25 lỗi hãng oan trên các lần thử S6. | Nguyễn Duy Mạnh |
| 2 · Dữ liệu | Chưa | B3 và C3.2 xác định tracking theo kiện là nguồn đối chiếu. `S6-04@11` cho thấy lệnh ghi không dùng nhất quán cùng một kiện. Còn phải xác minh các file khóa vì log báo `integrity` chưa đạt. | Nguyễn Duy Mạnh |
| 3 · Bảo mật | Chưa | Report S6 có 0 lần lộ PII. Trace S6-04@11 xác nhận đã lọc ghi chú khách trước khi gửi hãng. Cần thử riêng ca ghi chú chứa dữ liệu cá nhân theo B4. | Nguyễn Duy Mạnh |
| 4 · Quyền hạn | Chưa | `S6-20@11` ghi trước khi xác minh. Loạt `S6-LOAT` ghi 4 lỗi GHSH trong cùng ngày giả lập dù trần là 2 lỗi tự động/hãng/ngày. | Nguyễn Duy Mạnh |
| 5 · Hiệu năng, hạ tầng | Chưa | Report có 1 người, 6 ca/giờ, chờ tối đa 0 phút và 0 ca ùn khi tỷ lệ chuyển người bằng 0. Cần đo lại khi chuyển các ca mơ hồ và ca vượt trần sang người. | Đỗ Triệu Đức Phương |
| 6 · Chi phí | Chưa | S6 hiện 3.162đ/ticket so với 10.000đ làm tay, ROI 0,74. Cần đo lại chi phí khi các ca S6 cần xác minh thực sự vào hàng duyệt. | Vũ Xuân Bách |
| 7 · Vận hành | Chưa | Đã viết runbook 4–5 bên dưới. Log báo chưa có monitor mới, chưa có bằng chứng diễn tập cảnh báo và dừng trong 5 phút. | Đỗ Triệu Đức Phương |
| 8 · Con người, pháp lý | Chưa | S6 còn 25 lỗi ghi oan, GHSH có 20; 0 lần lộ PII trong report. Đối chiếu và xử lý với hãng theo C10 và Runbook 4. | Đỗ Triệu Đức Phương |
| 9 · Quyết định | Chưa | Report ghi chưa đủ căn cứ chọn Tiếp tục vì còn vi phạm ngưỡng đã ký. Chờ lần tự kiểm tra hợp lệ và quyết định ở C12. | Vũ Xuân Bách |


### Runbook 4 · Sau sự cố trên thẻ (vòng 2)


| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | B7.5 đã có `wrongful_carrier_faults` từ report, đỏ từ 1 lỗi. Chỉ số này phát hiện lỗi trong đánh giá sau khi có bản ghi. Cảnh báo sớm cần đối chiếu mã kiện/hãng/tài xế và độ trễ ngay trước lệnh ghi, cùng số lỗi hãng đã có trong ngày. Log báo chưa có monitor mới. |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Giữ ngưỡng đỏ từ 1 lỗi oan, SLA 60 phút và thời hạn dừng 5 phút. Đề xuất thêm hai điều kiện trước ghi: từ 1 sai lệch trong bộ khóa theo kiện thì chặn, và từ lỗi thứ 3 của cùng hãng trong ngày thì chuyển người (trần nghiệp vụ đã có là 2). Log hiện tại chưa xác nhận hai điều kiện đã hoạt động. |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Report vẫn 1 người, 6 ca/giờ. Hạnh đứng tên duyệt và gọi hỗ trợ theo ngưỡng giờ cao điểm, Tùng giữ công tắc, Oanh đối soát với hãng. Đo lại hàng chờ sau khi các ca mơ hồ và vượt trần được chuyển người. |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Report vẫn có độ phủ 100% và kiểm lại 0%. Khi xử lý sự cố, Tùng tạm tắt `file_carrier_fault` và `notify_carrier` theo B7.5. Nếu xác nhận hoàn sai hoặc không xác định được kiện cho khoản hoàn, tạm tắt luồng hoàn liên quan và chuyển tay. Oanh đối soát từng bản ghi nghi vấn theo đơn, kiện, hãng, tài xế và lưu căn cứ điều chỉnh trước khi mở lại. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | Đề xuất Hạnh phối hợp Đối tác báo đầu mối hãng có bản ghi nghi vấn trong vòng 1 giờ sau xác nhận. Nêu mã kiện và bản ghi cần rà, đề nghị treo việc dùng các lỗi đó để tính thưởng hoặc phạt trong lúc Oanh đối soát. Sau khi xác minh, gửi lại kết quả điều chỉnh. Hạnh báo người duyệt ca nào cần xử lý tay và tránh hoàn lần nữa trước khi đối chiếu sổ. |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Report ghi `pii_leaks = 0` ở cả ba mốc. Trace `S6-04@11` cho thấy `customer_note` và `district` bị lọc trước khi gửi, payload còn mã đơn, mã kiện và độ trễ. Nếu phát hiện payload thực có dữ liệu cá nhân, báo Tùng và đầu mối phụ trách dữ liệu nội bộ, lưu bằng chứng và tắt `notify_carrier`. |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Trên thẻ, tín hiệu đầu tiên là phản ánh của trưởng nhóm tài xế Sông Hồng qua phòng Đối tác. Report và trace cho thấy số bản ghi sai và vị trí lệch. Chưa có sổ thưởng thực tế để xác nhận số tiền bị trừ, dữ liệu khiếu nại liên tục hay monitor mới tự báo. |


### Runbook 5 · Ba kịch bản “nếu … thì …” cho tuần đầu chạy thử thật


1. Nếu số ticket tăng gấp **3 lần** trong một giờ, Hạnh theo dõi các ca thực sự cần duyệt và gọi hỗ trợ khi có từ **3 ca đang chờ** hoặc ca lâu nhất chờ **30 phút**. Nếu chờ quá **60 phút** hoặc có ca bị ùn, Tùng thu hẹp pilot, hoặc tắt `issue_refund` và chuyển CSKH nếu chưa thu hẹp được.
2. Nếu nhà cung cấp LLM lỗi quá **5 phút** (ngưỡng đề xuất), Tùng dừng nhận ticket tự động, tắt thao tác ghi và chuyển CSKH xử lý tay. Với ticket chưa rõ đã ghi hay chưa, Oanh đối chiếu sổ hoàn và sổ lỗi trước khi ai đó thực hiện lại. Chỉ mở lại sau khi Tùng xác nhận dịch vụ ổn định và kiểm tra ca mẫu.
3. Nếu người duyệt báo không tin một quyết định, Hạnh giữ ca để xác minh mã kiện, tracking và chính sách, kiểm sổ nếu đã phát sinh lệnh ghi, rồi ghi lại căn cứ xử lý. Nếu xác nhận có từ **1 lỗi oan**, Tùng tắt `file_carrier_fault` và `notify_carrier` trong tối đa **5 phút**, Oanh rà các bản ghi liên quan trước khi đề nghị mở lại.


---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | (giống v1: commit `Sign acceptance criteria`, hash tiêu chí `59429024`) |
| Hash chốt cổng vòng 1 | `a9e2211a` |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: `R-S6-before-20261119-170901-005ba4` · prepared: `R-S6-prepared-20261119-170901-005ba4` · after: `R-S6-after-20261119-170901-005ba4` |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Không (`vượt trần: không`). |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | Trên S6 các phân khúc đều đạt `pass = 1.0`, `oan = 0`; trên bộ nền có nhóm kho `?` (`chi phí 10.359đ > làm tay 10.000đ`, 5 trials). Quyết định không đổi nhưng cần theo dõi thêm chi phí các ca thiếu mã kho. |
| Quyết định (khoanh một) | **Tiếp tục** · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | `R-S6-after-20261119-170901-005ba4`: đạt toàn bộ chỉ số bắt buộc trên S6 (`pass_rate = 1.0`, `pass_k = 1.0`, `wrongful_refund_vnd = 0`, `wrongful_carrier_faults = 0`, `pii_leaks = 0`). |
| Bằng chứng 2 | Bộ nền (`regression`): giữ nguyên `pass_rate = 1.0`, `pass_k = 1.0`, `0đ` hoàn sai, `0` lỗi hãng oan. |
| Bằng chứng 3 | Kinh doanh & vận hành trên S6: `cost_per_ticket = 4.752đ <= 10.000đ`, `ROI = 1.1 >= 0.0`, `queue_stuck = 0`, `multi_parcel_guard_rate` sáng đèn (`0.0 -> 0.666667`). |
| Khớp dòng nào trong `decision_rule` đã ký? | Khớp dòng `Tiếp tục`: mọi chỉ số bắt buộc đạt trên cả bộ nền và gói sự cố, không vượt trần kinh doanh/vận hành. |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | (không áp dụng) |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | (không áp dụng) |
| Nếu Dừng: bài học ghi lại | (không áp dụng) |
| Ngày quyết định lại (trừ khi Dừng) | `2026-11-26 (sau 1 tuần pilot)` |
| PIC ký | `Vũ Xuân Bách` |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: **Giữ nguyên `Tiếp tục`** vì sau khi sửa ở vòng 2, gói sự cố S6 đạt `pass_rate = 1.0`, `wrongful_refund_vnd = 0`, `wrongful_carrier_faults = 0` và bộ nền không bị regression.
- Report tự kiểm tra: mã lần chạy `R-S6-grade-20261119-170901-005ba4` · ô nào còn đỏ (nguyên nhân × tầng): các ô `criteria`, `visible`, `regression`, `monitor` đều xanh (`✅`).
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: Đỡ được `15` lỗi hãng oan (`40 -> 25`), nhưng bỏ sót việc đơn tách nhiều kiện lấy nhầm `parcels[0]`, đơn nhiều kiện trễ thiếu `parcel_id`, và trần lỗi/hãng/ngày.
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: Report ghi **"Được phép cân nhắc 'Tiếp tục'"** — hoàn toàn khớp với quyết định của bàn.
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: Chưa đo được trên bài kiểm tra ẩn và lưu lượng đơn tách kiện thực tế ngoài mock; nếu tỉ lệ `escalated` tăng cao khi chạy thật sẽ cần bổ sung người duyệt hoặc thu hẹp phạm vi.

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: Thiết kế hiện tại giả định dữ liệu tracking DB luôn ghi nhận chính xác kiện nào bị trễ và đúng mã hãng vận chuyển cho từng kiện.
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: Các cổng trong `guards.py` thực sự NGĂN được tác hại ghi lỗi oan cho hãng giao đúng hẹn trong phạm vi tracking DB đúng, vì mọi lệnh ghi đều bị ép đối chiếu `ticket_parcel`, kiểm tra trần lỗi/ngày và chuyển người duyệt khi mơ hồ trước khi ghi sổ.
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: Cần đo lại tỉ lệ đơn tách nhiều kiện thiếu `parcel_id`, tỉ lệ chuyển người duyệt (`escalation_rate`), thời gian chờ hàng đợi CSKH và độ chính xác của tracking DB ngoài thực tế.
