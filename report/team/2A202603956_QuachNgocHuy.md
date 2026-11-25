# Báo cáo cá nhân — QuachNgocHuy-2A202603956

## 1. Thông tin thành viên

- Họ tên: Quách Ngọc Huy
- MSSV: 2A202603956
- Email: zellsed123@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi ở CP3 theo 5 loại của Google PAIR trong `report/team/bang_loi.md`, sau đó đối chiếu với Người gắn nhãn 1 để tính tỉ lệ đồng thuận, viết quy tắc phân biệt và hoàn thiện bảng khắc phục 5 ca.
- Giữ và cập nhật hồ sơ tổng hợp `report/team/ho_so_launch_v0.md` theo tiến độ các checkpoint CP1–CP5.

## 3. Đóng góp cụ thể

- Đã hoàn thành gắn nhãn độc lập toàn bộ 20 ca lỗi (cột `Nhãn người 2`), đối chiếu đạt đồng thuận 20/20 (100%) và hoàn thiện bảng khắc phục 5 ca theo 5 loại Google PAIR trong `report/team/bang_loi.md`.
- Đã cập nhật đầy đủ 7/7 mục và đề xuất `Go có điều kiện` trong hồ sơ `report/team/ho_so_launch_v0.md`.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commit `e4c0876` (điền cột `Nhãn người 2`, bảng khắc phục 5 ca, hồ sơ 7 mục), `b579406` (sửa hồ sơ: 0,49×, power 0,64, người phụ trách và ngày kiểm tra cho từng điều kiện).
- `report/team/bang_loi.md`: cột `Nhãn người 2` cho 20 ca; bảng khắc phục ca 1, 20, 16, 19, 5 (cột khắc phục và người phụ trách).
- `report/team/ho_so_launch_v0.md`: 7 mục và đề xuất Go có điều kiện với 3 điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra.
- Con số trong hồ sơ lấy từ `src/lab13.py` của nhóm: 4.472 đ mỗi việc thành công, 5.865 đ = 0,49× cả hệ thống, n = 859 mỗi nhóm, power 0,64 [simulated ở các số chi phí].

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- **Claude Code** (trong VS Code): soạn nháp nội dung hồ sơ và bảng khắc phục; rà soát hồ sơ, đối chiếu với đề bài, `RUBRIC.md` và các file của nhóm để tìm chỗ mâu thuẫn; giải thích lại 5 loại lỗi PAIR và cách phân biệt các ca dễ nhầm.
- Cách tự kiểm tra:
  - Chạy `python lab13.py` trong `src/`, đối chiếu từng con số trong hồ sơ với kết quả in ra và với `bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml`.
  - Đối chiếu mô tả 20 ca trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` với định nghĩa 5 loại lỗi; kiểm tra mỗi dòng khắc phục có event, ngưỡng và một vai trò phụ trách.
  - Kiểm tra không có từ cấm theo quy tắc 5 của `README.md` trong hồ sơ; mọi mục dựa trên cột `_simulated` ghi trạng thái Giả lập.

## 6. Tự đánh giá

- Làm được: hồ sơ đủ 7 mục, mỗi mục có con số, trạng thái và một vai trò; đề xuất nêu con số bất lợi (power 0,64) và cách xử lý; bảng khắc phục đủ 5 loại.
- Hạn chế: bảng khắc phục ban đầu giao chưa đúng vai cho ca 1, 16, 5; đã đổi sang vai có quyền sửa. Phút xem lại và làm lại trong hồ sơ vẫn là số simulated, cần thay bằng phút đo thật sau tuần 1 của pilot.
