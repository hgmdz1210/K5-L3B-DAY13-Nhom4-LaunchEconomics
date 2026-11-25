# Báo cáo cá nhân — DoanSyHung-2A202603990

## 1. Thông tin thành viên

- Họ tên: Đoàn Sỹ Hưng
- MSSV: 2A202603990
- Email: hungizumi1210@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code

## 2. Phần việc phụ trách

- Viết và chạy `src/lab13.py` cho CP1 (Nhiệm vụ A), CP2 (Nhiệm vụ B), phần tính cỡ mẫu D1 của CP4 và ba chỉ số tính thử E1 của CP5.
- Điền các file hồ sơ dựa trên kết quả của code: `report/team/bang_chi_phi.md` (A, B), `report/team/pilot_plan.yaml` (D) và `report/team/chi_so.md` (E).
- Rà soát và chỉnh phần bảng khắc phục của CP3 sau khi hai người gắn nhãn nộp bảng, để cách phát hiện đo được bằng event có trong `chi_so.md`.

## 3. Đóng góp cụ thể

- **`src/lab13.py`:**
  - ba hàm A1 và hàm `mo_hinh` (tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`);
  - bảng theo loại yêu cầu (A3), chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (A4);
  - 9 kịch bản độ nhạy kèm kiểm tra "giảm một nửa = nửa mức tăng" (B1), kịch bản một cặp và xếp hạng (B2), chi phí cả hệ thống theo giới hạn chạy (B3), xem lại 100% (B4);
  - cỡ mẫu theo ba cách chia, hệ số thiết kế và power (D1); ba chỉ số E1.
  - Thêm `sys.stdout.reconfigure(encoding='utf-8')` để chạy được trên console Windows.
- **`bang_chi_phi.md`:** điền đủ A1–A4 và B1–B4, mọi số tính từ cột `_simulated` có nhãn `simulated`. Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ).
- **`pilot_plan.yaml`:** chọn chia theo nhân viên 20 + 20, mức chênh 6 điểm (n = 859 mỗi nhóm, DE = 6,96, 20 cụm mỗi nhóm), ghi đánh đổi power khoảng 0,64 nếu tác động thật là 5 điểm; viết 4 luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ.
- **`chi_so.md`:** ba chỉ số tính thử (chính 82,83%, dùng 27,12%, an toàn 4,25%), hai chỉ số tự đề xuất, 11 event có `trace_id`, 4 dòng rủi ro kinh tế lấy số từ bảng độ nhạy.
- **`bang_loi.md`:** không gắn nhãn (phần của hai người gắn nhãn). Chỉ chỉnh cột "Phát hiện bằng gì" của ca 1, 20, 16 và thêm event `notification_sent`, thuộc tính `request_id` cho `refund_ledger_write` trong `chi_so.md`.
- Đưa các file về đúng khung mẫu: rút câu trả lời xuống tối đa ba dòng, bỏ phần ngoài mẫu, thêm nhãn simulated còn thiếu.

## 4. Bằng chứng

- Commit trên nhánh `main`: `3bd9d03` (hoàn thành phần người viết code CP1, CP2, CP4, CP5), `5afef7a` (đưa `bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml` về đúng khung mẫu), `48d1b09` (chỉnh bảng khắc phục ca 1, 20, 16 và event trong `chi_so.md`).
- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`.
- Con số do code tính ra (simulated nếu có tiền xem lại hoặc làm lại):

| Nội dung | Kết quả |
| --- | --- |
| Ba phép thử A1 (p = 0,8) | 1,20 · 1,25 · 1,25, ĐẠT |
| Chi phí mỗi việc thành công | 4.472 đ; gấp 16,3 lần hoá đơn token |
| Chi phí cả hệ thống mỗi yêu cầu | 5.865 đ = 0,49× của 12.000 đ |
| Xếp hạng độ nhạy | Số ca làm lại +51,8% · xem lại +40,7% · lương +23,1% |
| Giới hạn chạy lại rẻ nhất cho công ty | 2 lần, 6.901.220 đ |
| Xem lại 100% (noi_dia + hang_nang) | 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút) |
| Cỡ mẫu D1 | 1.251 · 3.103 · tối đa 1.000 · tối đa 300 · m ≥ 299 |

## 5. Công cụ AI đã dùng

- **Claude Code** (trợ lý AI trong VS Code): hỗ trợ đọc repo và tài liệu, hỗ trợ viết `src/lab13.py`, soạn nháp các bảng trong `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`, và rà soát file của các thành viên khác đối chiếu với đề bài.
- Cách tự kiểm tra:
  - Chạy `python lab13.py` trong `src/`, phải thoát với mã 0 và in ba phép thử A1 là ĐẠT.
  - Đối chiếu từng con số (A2, A3, A4, B1–B4, D1, E1) với số đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; lệch không quá 2% (B4 ở mức 15,3 phút lệch 1 đ do làm tròn).
  - Mã có sẵn phép kiểm tra tự động: kịch bản "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi".
  - `yaml.safe_load` đọc được `pilot_plan.yaml`, không còn dấu `?` ngoài chú thích, mỗi luật dừng đủ bốn vế; `grep` không thấy từ bị cấm (quy tắc 5 của lab) trong file hồ sơ.
  - Đối chiếu nội dung các file với `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và `docs/Ngay13_Huong_dan_hoc_vien.docx`.

## 6. Tự đánh giá

- Làm được: mô hình chi phí tính từ trace khớp đáp án mẫu; kế hoạch pilot có nhóm đối chứng, đủ cỡ mẫu theo cụm và luật dừng có ngưỡng.
- Hạn chế: toàn bộ chi phí xem lại và làm lại dựa trên cột `_simulated`, nên các con số chi phí đều là giả lập. Pilot không đủ mẫu để thấy mức chênh 5 điểm, nên phải chấp nhận mức chênh 6 điểm với power khoảng 0,64.
