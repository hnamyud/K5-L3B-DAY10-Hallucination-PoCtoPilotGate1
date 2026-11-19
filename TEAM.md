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

## VuXuanBach-2A202603803

### Phần việc phụ trách

Vai **Sản phẩm và Kinh doanh**
- **Vòng 1:** 
  - Phiếu A: Câu 1.1 (Mục A1), Câu 1.5 (Mục A3), Câu 1.6 (Mục A4 & A5).
  - Cấu hình & ký: `config/acceptance_criteria.json` và `.lock`.
  - Phiếu B: Câu 2.3 (Mục B3 - Bản đồ dữ liệu & Data Drift), Câu 2.5 (Mục B6 - Pre-mortem lăng kính kinh doanh), Câu 2.9 (Mục B7.4, điền mục `business` trong `config/operating_gates.json`), tổng hợp Quyết định v1 (Mục B8).
- **Vòng 2 (Thẻ S6):**
  - Phiếu C: Đọc khối kinh doanh/vận hành (Mục C1), Câu 3.2 (Mục C5 - Specification & Giả định môi trường), Câu 3.5 (Mục C6 & C7 - Nhánh kinh doanh & điều chỉnh cổng `business`), tổng hợp Quyết định v2 và 3 dòng bắt buộc (Mục C12).

### Đóng góp cụ thể

- Xác định mục tiêu hệ thống cấp cao (Câu 1.1), phân tích khoảng tin cậy 95% (Câu 1.5 chọn đáp án b) và hoàn thiện Bản tiêu chí chấp nhận với các ngưỡng an toàn tài chính trong `config/acceptance_criteria.json` trước khi chạy đánh giá lần đầu.
- Lập bản đồ dữ liệu và phân tích hiện tượng Data Drift (Câu 2.3 khi chuyển từ chính sách bồi thường `REFUND-v3` sang `REFUND-v4` ngày 01/12/2026).
- Thiết lập các cổng kiểm soát kinh doanh trong `config/operating_gates.json`, giải trình chi tiết ở Mục B7.4 và cùng nhóm chốt Quyết định Gate 1 v1 ở Mục B8.
- Xử lý sự cố thẻ S6: Phân tích nguyên nhân tài xế Sông Hồng (GHSH) bị phạt oan do lỗi tách đơn đa kiện (`multi-parcel`), viết đặc tả hệ thống (Câu 3.2) và đề xuất tầng can thiệp kinh doanh/phạm vi pilot (3.5).
- Đánh giá tác động tài chính của sự cố S6 (270k hoàn sai tập trung ở Kho HCM, 40 lỗi hãng oan cho GHSH và DNB) để cùng nhóm chốt Quyết định Gate 1 v2 và 3 dòng bắt buộc ở Mục C12.

### Bằng chứng

- Commits: `44d1d4b` (chốt cổng vòng 1, quyết định v1), `a3f5c95` (nhận thẻ S6), `bdc2020` (cập nhật checklist), `b3c7f12` (nộp vòng 2).
- Mã lần chạy: `R-S6-grade-20261119-173059-005ba4` (`lab10.check_submission --collect` báo `ĐỦ THÀNH PHẦN`).
- Phiếu: Phiếu A (A1, A2), Phiếu B (B4, B5, B7.5–B7.6), Phiếu C (C3.2, C4, C5, C9–C11), `submission/submission.json`.

### Exit ticket

- **Một điều học được:** Một hệ thống AI trả lời mượt mà và có accuracy cao trong lab vẫn có thể gây thảm họa tài chính và pháp lý ngoài đời thực nếu không có các cổng kiểm soát trần tiền , trần chi phí và cơ chế đối soát chéo với nguồn sự thật.
- **Một điều còn chưa chắc:** Trong môi trường sản xuất thực tế với hàng nghìn đơn tách nhiều kiện phức tạp, ranh giới giữa việc "tự động hóa để tiết kiệm chi phí" và "chuyển người duyệt để đảm bảo an toàn" cần được cân đối thế nào để không làm vỡ trận hàng chờ của đội ngũ CSKH trong các mùa siêu sale.

## DoTrieuDucPhuong-2A202603843

### Phần việc phụ trách

Vai **Vận hành và Pháp lý** — Vòng 1: Câu 1.2, 1.4 (Phiếu A mục A1, A2), Câu 2.4 (Phiếu B mục B4 HAZOP vòng 1, B5 checklist 9 nhóm việc), Câu 2.10 (B7.5–B7.6 runbook phần 1–3 & giờ cao điểm, mục `operations` và `legal` trong `config/operating_gates.json`). Vòng 2 (thẻ S6): Ghi `Thẻ đã bốc: S6`, Câu 3.1 phần riêng C3.2 & HAZOP thẻ (C4), Câu 3.3 giả định môi trường (C5), Câu 3.7 cập nhật fault tree sau sửa (C9), Risk register (C10), cập nhật checklist & runbook phần 4–5 (C11), điền `submission/submission.json` và chạy `lab10.check_submission --collect`.

### Đóng góp cụ thể

- Thiết kế mục tiêu cho kế toán đối soát & trưởng ca CSKH (`1.2`), telemetry production (`1.4`), HAZOP vòng 1 và checklist 9 nhóm việc có PIC (`2.4`).
- Đặt cổng `operations` (`pic: NV-TUNG`, `approver_id: NV-HANH`, SLA 60 phút, điều kiện dừng) và `legal` (chặn PII gửi bên thứ ba, yêu cầu `delay_cause`) trong `config/operating_gates.json`, viết runbook phần 1–3 & giờ cao điểm (`2.10`).
- Vòng 2 (S6): Hoàn thiện C3.2 (Hình dung của người và của hệ thống), HAZOP thẻ (`C4`), giả định môi trường (`3.3`), cập nhật fault tree (`C9`), Risk register (`C10`), checklist & runbook phần 4–5 (`C11`), và gom bài nộp `submission/submission.json`.

### Bằng chứng

- Commits: `44d1d4b` (chốt cổng vòng 1, quyết định v1), `a3f5c95` (nhận thẻ S6), `bdc2020` (cập nhật checklist), `b3c7f12` (nộp vòng 2).
- Mã lần chạy: `R-S6-grade-20261119-173059-005ba4` (`lab10.check_submission --collect` báo `ĐỦ THÀNH PHẦN`).
- Phiếu: Phiếu A (A1, A2), Phiếu B (B4, B5, B7.5–B7.6), Phiếu C (C3.2, C4, C5, C9–C11), `submission/submission.json`.

### Exit ticket

- Điều rút ra từ S6: Cổng kiểm nguyên nhân trễ vẫn có thể để lọt lỗi nếu dữ liệu dùng để tính độ trễ và bản ghi quy trách nhiệm thuộc hai kiện khác nhau.
- Điều cần kiểm chứng: Sau khi chuyển các ca thiếu căn cứ sang người duyệt, một người trực với công suất 6 ca/giờ có giữ được SLA 60 phút trong giờ cao điểm hay không.