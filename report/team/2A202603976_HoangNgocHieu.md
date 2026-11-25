# Báo cáo cá nhân — Hoàng Ngọc Hiệu

## 1. Thông tin thành viên

- Họ tên: Hoàng Ngọc Hiệu
- MSSV: 2A202603976
- Email: hoangngochieu10012000@gmail.com
- Vai trong nhóm: Người kiểm số

## 2. Phần việc phụ trách

Đối chiếu số A2/A3/B/D1 từ dữ liệu CSV và công thức của lab, độc lập với kết quả tính trong `src/lab13.py`.

## 3. Đóng góp cụ thể

- Đối chiếu hai CSV: tổng chi phí, số việc thành công, chi phí theo loại, độ nhạy, giới hạn chạy lại, cỡ mẫu và tỉ lệ mở lại.
- Kiểm tra tổng token/tool, chi phí xem lại/làm lại (đánh dấu simulated), số việc thành công và chi phí mỗi việc thành công.
- Tính riêng kết quả A3 theo bốn loại yêu cầu; tính B1 và chi phí toàn hệ thống cho giới hạn 1, 2, 3 lần chạy.
- Tính D1 cho mức chênh 5 và 6 điểm, số yêu cầu tối thiểu mỗi nhân viên khi chia 20 nhân viên mỗi nhóm; kiểm tra tỉ lệ mở lại 7 ngày.

## 4. Bằng chứng

Kết quả kiểm tra trên CSV:

```text
Token                    245,585
Tool                     84,000
Run thu 2-3 (token+tool) 93,804
Xem lai [simulated]      1,780,000
Lam lai [simulated]     2,264,000
Tong [co simulated]     4,373,585
So viec thanh cong      978
Chi phi/viec thanh cong 4,471.97
n/arm for +5 percentage points: 1,251
n/arm for +6 percentage points: 859
Requests/staff for +6pt with 20 staff/arm: 299
Safety reopen rate: 51/1200 = 4.25%
KET LUAN: Tat ca assertion kiem tra doc lap deu DAT.
```

Kết quả A3 khớp hướng dẫn: chi phí mỗi việc thành công là 2.696 đ (`noi_dia`), 8.221 đ (`hang_nang`), 22.515 đ (`quoc_te`) và 10.215 đ (`doi_tac`). Tỉ lệ run `quoc_te` thành công theo attempt giảm từ 30,0% xuống 11,4% rồi 2,2%.

### Cách tự kiểm lại bằng bảng tính

- Thêm cột chi phí token cho mỗi run: `tokens_in × 26 / 1000 + tokens_out × 130 / 1000`; cột tool: `tool_calls × 15`; cộng cả hai cho mọi run.
- Trong bảng request, cộng phút xem lại và làm lại rồi nhân riêng từng tổng với 2.000 đ/phút. Hai tổng này là `simulated`.
- Chia tổng bốn khoản cho số request có `ket_qua = thanh_cong`; hóa đơn đơn giản là `(token + tool) / 1.200`.
- A3: lọc từng `loai`, cộng đúng bốn khoản trên trong phạm vi lọc rồi chia số thành công. Ví dụ `noi_dia`: `2.110.687 / 783 = 2.696 đ`.
- B1: thay một khoản trong tổng A2 theo kịch bản rồi chia lại cho 978. Ví dụ làm lại ×2: `(4.373.585 + 2.264.000) / 978 = 6.787 đ`.
- B3: lọc run theo `attempt ≤ k`; cộng chi phí trợ lý, rồi cộng `12.000 × số yêu cầu không thành công` để ra chi phí hệ thống.
- D1: dùng công thức cỡ mẫu hai tỉ lệ; sau đó nhân hệ số cụm `1 + (m − 1) × 0,02`. Với 20 cụm và mức +6 điểm, giải `20m / (1 + (m − 1) × 0,02) ≥ 859`, được `m = 299`.

## 5. Công cụ AI đã dùng

Copilot hỗ trợ đối chiếu số liệu và soạn báo cáo. Helper dùng để kiểm tra ban đầu chỉ là file cục bộ và được thêm vào `.gitignore`, không phải deliverable nộp. Các phép tính tay cần được trình bày bằng cách cộng/đếm các cột CSV theo công thức của lab.

## 6. Tự đánh giá

Đã có bảng số đối chiếu A2/A3/B và D1. Cần tự làm lại các phép tính tay, đối chiếu với đầu ra cuối cùng của `lab13.py`, rồi chép số đã thống nhất vào hồ sơ nhóm trước khi nộp.
