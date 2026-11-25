# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Nhóm 4
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN (dữ liệu giả lập) để trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào. Cách làm: tính chi phí thật từ trace (tử số tính mọi lần chạy, mẫu số chỉ đếm việc thành công), tìm yếu tố nhạy nhất, phân loại lỗi, rồi thiết kế pilot có nhóm đối chứng và luật dừng.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- **A, B:** `src/lab13.py` tính mô hình chi phí, bảng theo loại, chi phí cố định và 9 kịch bản độ nhạy. Kết quả ở [bang_chi_phi.md](bang_chi_phi.md).
- **C:** hai người gắn nhãn 20 ca lỗi theo 5 loại của Google PAIR, rồi chọn 5 ca (mỗi loại một ca) để lập bảng khắc phục đo được bằng event. Kết quả ở [bang_loi.md](bang_loi.md).
- **D:** cỡ mẫu theo ba cách chia, chọn chia theo nhân viên 20 + 20, viết 4 luật dừng. Kết quả ở [pilot_plan.yaml](pilot_plan.yaml).
- **E:** ba chỉ số tính thử, 11 event có `trace_id`, rủi ro kinh tế ở [chi_so.md](chi_so.md); hồ sơ một trang ở [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- Chi phí mỗi việc thành công: **4.472 đ** [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ). Cả hệ thống 5.865 đ mỗi yêu cầu = 0,49× của 12.000 đ [simulated]. Trong phạm vi `noi_dia` + `hang_nang` cộng chi phí cố định: 4.599 đ = 0,38× [simulated].
- Ba yếu tố nhạy nhất [simulated]: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%). Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ). Xem lại 100% cho 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút).
- Pilot: chia theo nhân viên 20 + 20, mức chênh 6 điểm (n = 859 mỗi nhóm, DE = 6,96), power khoảng 0,64 nếu tác động thật là 5 điểm; phạm vi `noi_dia` + `hang_nang`.
- Chỉ số trong đợt chạy thử: chính 82,83%, dùng (bỏ qua gợi ý) 27,12%, an toàn (mở lại 7 ngày) 4,25%.
- **Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`.
- Kết quả duyệt chéo: chưa có (nhóm chưa được chấm tại thời điểm viết).

## 5. Khó khăn và cách xử lý

- Không cách chia nào đủ mẫu cho mức chênh 5 điểm với 40 nhân viên (tối đa 1.000 < 1.251); nhóm chọn mức chênh 6 điểm và ghi rõ đánh đổi.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Chi phí xem lại và làm lại dựa trên cột `_simulated`, nên các số chi phí đều là giả lập; cần thay bằng phút đo thật sau tuần 1 của pilot.
- Đợt chạy thử không có nhóm đối chứng, nên chỉ số 82,83% không chứng minh trợ lý đã nâng chỉ số; pilot phải trả lời việc này.
- Power chỉ khoảng 0,64 ở mức chênh 5 điểm; cải thiện bằng cách kéo dài bước 0.50 hoặc tăng số nhân viên.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", pair.withgoogle.com.
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`).
