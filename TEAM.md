# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Hallucination
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Hallucination-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S6

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |Nguyễn Duy Mạnh|2A202603806|Kỹ sư cổng|x|
|   2 |Vũ Xuân Bách|2A202603803|Sản phẩm và Kinh doanh||
|   3 |Đỗ Triệu Đức Phương|2A202603843|Vận hành và Pháp lý||

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## NguyenDuyManh-2A202603806

### Phần việc phụ trách

Vai **Kỹ sư cổng** — Vòng 1: Câu 1.3 (Phiếu A mục A2), Câu 2.1, 2.2, 2.6, 2.7, 2.8 (Phiếu B mục B0, B1, B2, B7.1–B7.3), chạy unit test và `lab10.checkpoint`. Vòng 2 (thẻ S6): Bước 0 (C0), Câu 3.1 (C2), Câu 3.5 (C7), Câu 3.6 (C8), chạy regression test và `lab10.grade --incident S6`. File chính: `lab10/guards.py`, `lab10/monitors.py`.

### Đóng góp cụ thể

- Thiết kế offline metric cho bước chọn chính sách (`1.3`).
- Chạy baseline, phân tích trace `T-002@55` (`2.1`, `2.2`); code 3 cổng vòng 1 trong `lab10/guards.py` (ghim `effective_policy`, chặn hoàn trùng qua `ledger_rows`, chặn hoàn sai & lỗi hãng oan theo tracking DB) và viết 2 behavioral test `--adhoc` (`2.6–2.8`).
- Vòng 2 (S6): Dò trace `S6-01@11`, `S6-20@11`, `S6-42@11` (`3.1`); bổ sung cổng `escalate` đơn nhiều kiện trễ thiếu `parcel_id`, `Verdict.modify` sửa đúng kiện/hãng trễ, và `Verdict.deny` khi vượt trần lỗi/hãng/ngày (`3.5`); thêm monitor `multi_parcel_guard_rate` trong `lab10/monitors.py` (`3.6`), đưa `pass_rate` trên S6 từ `0.3333` lên `1.0` (`0` lỗi oan, `0đ` hoàn sai).

### Bằng chứng

- Commits: `44d1d4b` (chốt cổng vòng 1 `a9e2211a`), `a3f5c95` (nhận thẻ S6), `b3c7f12` (nộp vòng 2).
- Mã lần chạy: `R-base-before-20261119-155123-bde05c` (base), `R-base-prepared-20261119-163624-b504cd` (prepared), `R-S6-grade-20261119-173059-005ba4` (grade S6).
- Phiếu: Phiếu A (A2), Phiếu B (B0–B2, B7.1–B7.3), Phiếu C (C0, C2, C7, C8).

### Exit ticket

- **Điều học được:** Các lỗi nguy hiểm nhất thường là lỗi chìm ở lớp hệ thống (lệch đơn vị đơn/kiện, thiếu kiểm tra sổ cái/trần vận hành), nên cần dựng guard và monitor độc lập bên ngoài model.
- **Điều còn chưa chắc:** Tỉ lệ đơn tách nhiều kiện thiếu `parcel_id` ngoài thực tế có thể cao hơn mock, dễ làm tăng tải hàng chờ CSKH khi chạy pilot thật.