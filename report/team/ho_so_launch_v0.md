# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Nhóm 4 · Lớp: L3B

| Mục                                           | Con số chính                                                                                                                                | Trạng thái          | Người phụ trách  |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ---------------- |
| 1 · Chi phí mỗi việc thành công               | 4.472 đ toàn mẫu; 3.414 đ trong phạm vi `noi_dia + hang_nang`; 4.599 đ (+cố định 45.000 yc/tháng)                                           | Giả lập             | Người viết code  |
| 2 · Ba yếu tố nhạy nhất                       | 1. Số ca làm lại (±51,8%) · 2. Tỉ lệ xem lại (±40,7%) · 3. Lương nhân viên (+23,1%)                                                         | Giả lập             | Người kiểm số    |
| 3 · So với nhân viên tự làm                   | 0,49× (5.865 đ cả hệ thống ÷ 12.000 đ); trong phạm vi `noi_dia + hang_nang` + cố định = 0,38×                                               | Giả lập             | Người kiểm số    |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính 82,83% (phạm vi 92,26%); Dùng (bỏ qua gợi ý) 27,12%; An toàn (mở lại 7 ngày) 4,25% (phạm vi 3,97%)                                    | Xong, có bằng chứng | Người viết code  |
| 5 · Bảng lỗi và cách khắc phục                | 20 ca (chờ Người gắn nhãn 1 xác nhận độc lập); đủ 5 loại PAIR + 5 cách khắc phục đo bằng event                                              | Xong                | Người gắn nhãn 2 |
| 6 · Pilot plan                                | Chia theo nhân viên 20 + 20, MDE 6 điểm (n = 859/nhóm, m ≥ 299, DE = 6,96; power 0,64 nếu chênh 5 điểm), 4 luật dừng, quyết định 2027-01-05 | Xong, có bằng chứng | Người viết code  |
| 7 · Rủi ro kinh tế                            | Làm lại ×2: +51,8% (6.787 đ); xem lại 100%: 11.743–12.415 đ; giảm nửa khối lượng: +2.370 đ/việc; 3 lần chạy đắt hơn 136.365 đ               | Giả lập             | Người viết code  |

**Đề xuất:** Go có điều kiện (chấp nhận đánh đổi: với 40 nhân viên, chọn MDE 6 điểm nên **power chỉ còn khoảng 0,64** nếu tác động thật là 5 điểm; xử lý bằng cách chạy bước 0.50 ít nhất 2 tuần để đủ `m ≥ 299` yêu cầu/nhân viên).

- Chỉ chạy pilot trong phạm vi `noi_dia + hang_nang` (loại `quoc_te`, `doi_tac`) và Giám đốc vận hành ký chấp nhận mức `power 0,64` ở chênh lệch 5 điểm — **Người phụ trách:** PM trợ lý hoàn phí · **Ngày kiểm tra:** trước bước `0.10` (`2026-12-01`).
- Sửa xong khoá chống trùng `idempotency_key` (ca 20) và bật kiểm mẫu 100 đơn/tuần (`audit_sample_checked`) — **Người phụ trách:** Kỹ sư trưởng agent · **Ngày kiểm tra:** trước bước `0.10` (`2026-12-01`); đánh giá tổng kết pilot ngày `2027-01-05`.
- Thay thế các cột phút `_simulated` bằng dữ liệu đo thật từ `staff_review_decision` và `staff_rework_completed`; Người gắn nhãn 1 xác nhận độc lập 20 ca — **Người phụ trách:** Trưởng nhóm CSKH & Người gắn nhãn 1 · **Ngày kiểm tra:** cuối tuần 1 / trước bước `0.25` (`2026-12-08`).
