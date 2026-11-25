# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Nhóm 4 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ toàn mẫu; 3.414 đ trong phạm vi `noi_dia + hang_nang`; 4.599 đ (+cố định 45.000 yc/tháng) | Giả lập | ... |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (±51,8%) · 2. Tỉ lệ xem lại (±40,7%) · 3. Lương nhân viên (+23,1%) | Giả lập | ... |
| 3 · So với nhân viên tự làm | 0,37× (4.472 ÷ 12.000 đ); cả hệ thống 5.865 đ = 0,49×; trong phạm vi + cố định = 0,38× | Giả lập | ... |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính 82,83% (phạm vi 92,26%); Dùng (bỏ qua gợi ý) 27,12%; An toàn (mở lại 7 ngày) 4,25% (phạm vi 3,97%) | Xong, có bằng chứng | ... |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, đồng thuận 20/20 = 100% (5 loại PAIR + 5 cách khắc phục đo bằng event) | Xong, có bằng chứng | Người gắn nhãn 2 |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, MDE 6 điểm (n = 859/nhóm, m ≥ 299, DE = 6,96), 4 luật dừng, quyết định 2027-01-05 | Xong, có bằng chứng | ... |
| 7 · Rủi ro kinh tế | Làm lại ×2: +51,8% (6.787 đ); xem lại 100%: 11.743–12.415 đ; giảm nửa khối lượng: +2.370 đ/việc; 3 lần chạy đắt hơn 136.365 đ | Giả lập | ... |

**Đề xuất:** Go có điều kiện

- Chỉ chạy pilot trong phạm vi `noi_dia + hang_nang` (loại `quoc_te` và `doi_tac`); Giám đốc vận hành ký chấp nhận đánh đổi MDE 6 điểm (`n = 859/nhóm`) trước ngày bắt đầu.
- Sửa xong khoá chống trùng `idempotency_key` (ca 20) và bật kiểm mẫu 100 đơn/tuần (`audit_sample_checked`) trước khi bật bước `0.10`; kiểm tra lại toàn bộ vào ngày `2027-01-05` (PM trợ lý hoàn phí & Kỹ sư trưởng agent).
- Thay thế các cột phút `_simulated` bằng dữ liệu đo thật từ `staff_review_decision` và `staff_rework_completed` sau tuần 1 (Trưởng nhóm CSKH).
