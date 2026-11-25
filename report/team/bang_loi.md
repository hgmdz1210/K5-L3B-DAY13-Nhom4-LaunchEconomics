# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Lê Thị Ly · Người gắn nhãn 2: Quách Ngọc Huy (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca không trùng (đồng thuận 20/20 = 100%).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | `refund_ledger_write` có `ket_qua` là lỗi từ ngân hàng (sai số tài khoản) > 2% số yêu cầu/tuần | Kiểm tra độ dài và định dạng số tài khoản ngay trên form trước khi gửi; hiển thị hướng dẫn nhập đúng | Kỹ sư trưởng agent |
| 20 | Hệ thống | Đối soát hằng giờ `refund_ledger_write`: ≥ 2 bản ghi cùng `request_id`, hoặc bản ghi thiếu `idempotency_key` (ngưỡng ≥ 1 ca) | Bắt buộc gắn `idempotency_key` theo `request_id` ở sổ cái và khoá nút gửi lại khi đang xử lý | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | `notification_sent` có `sent_at` ngoài 07:00–21:00 (ngưỡng 0 thông báo/ngày), hoặc `ticket_reopened` với `reason` là bị làm phiền ngoài giờ > 1%/tuần | Hạn chế gửi thông báo Zalo khung 21:00–07:00, dời sang 07:30 sáng hôm sau | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | `handoff_to_staff` với lý do ngoài dữ liệu 12 tháng hoặc ngoài phạm vi > 5%/tuần | Nhận diện sớm giới hạn dữ liệu/phạm vi ở lần chạy 1, thông báo rõ cho khách và chuyển nhân viên kèm tóm tắt | PM trợ lý hoàn phí |
| 5 | Ngầm | `audit_sample_checked` hằng tuần (100 đơn/tuần) thấy `so_tien_da_hoan != so_tien_dung` > 1% mẫu | Đối soát tự động giá sau mã giảm giá trước khi gọi `refund_ledger_write` và duy trì kiểm mẫu hằng tuần | PM trợ lý hoàn phí |
