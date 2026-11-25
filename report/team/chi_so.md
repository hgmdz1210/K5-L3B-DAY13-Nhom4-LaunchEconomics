# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py` (mục E1). Mọi số tính từ cột `_simulated` ghi nhãn `simulated`.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200); trong phạm vi noi_dia + hang_nang: 92,26% |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); trong phạm vi noi_dia + hang_nang: 3,97% |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được nhân viên mở bằng trợ lý | Số yêu cầu có `agent_suggestion_shown` ÷ số yêu cầu gán cho nhân viên nhóm trợ lý, theo tuần | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | `so_tien_da_hoan` khác `so_tien_dung` ÷ số đơn trong mẫu 100 đơn mỗi tuần | Không cần tính |

Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số từ 0,70": đợt chạy thử không có nhóm đối chứng. Baseline 0,70 là số của công ty, không phải số của đợt chạy thử.

Trong phạm vi noi_dia + hang_nang, chỉ số chính cao hơn (92,26%) và tỉ lệ mở lại thấp hơn một chút (3,97%) so với cả mẫu. Cả 51 ca mở lại đều thuộc nhóm `lam_lai` (51/74 ca làm lại); không ca `thanh_cong` hay `chuyen_nhan_vien` nào bị mở lại.

## Danh sách event

Mười event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, arm, staff_id (gán lúc vào hàng đợi), created_at, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ |
| `handoff_to_staff` | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, event dùng để tính:

- Chỉ số chính: `refund_request_created` (created_at) + `ticket_closed` (closed_at) để biết đóng trong 24 giờ, và `ticket_reopened` để loại ca mở lại trong 7 ngày. Đo được.
- Chỉ số dùng (bỏ qua gợi ý): `staff_review_decision` (đếm `sua` và `bo` trên tổng số quyết định). Đo được.
- Chỉ số an toàn (mở lại 7 ngày): `ticket_reopened` chia số `refund_request_created`. Đo được.
- Chỉ số dùng tự đề xuất (% yêu cầu được mở bằng trợ lý): `agent_suggestion_shown` chia `refund_request_created` có `arm` bằng nhóm trợ lý. Đo được.
- Chỉ số an toàn tự đề xuất (đơn hoàn sai tiền): `audit_sample_checked`, đối chiếu `refund_ledger_write` cùng trace_id. Đo được.
- Chi phí mỗi việc thành công (luật dừng): `agent_run_completed` cho token và tool, `staff_review_decision` và `staff_rework_completed` cho phút thật. Hiện cột phút trong mẫu là simulated, phải thay bằng phút đo thật sau tuần 1.
- Luật dừng hoàn trùng: `refund_ledger_write` có hai bản ghi cùng `idempotency_key` hoặc cùng request_id. Đo được.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy (`bang_chi_phi.md`). Tất cả số tiền là simulated.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ mỗi việc thành công (từ 4.472 đ) [simulated] | Tỉ lệ làm lại theo tuần vượt 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98x của 12.000 đ; 12.415 đ = 1,03x nếu làm lại 15,3 phút như dữ liệu (hoà vốn xem lại ≤ 5,1 phút, hoặc ≤ 4,8 phút) [simulated] | % yêu cầu được xem lại còn trên 50% cuối bước 0.25 (đợt chạy thử: 14,75%) | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ dưới 15% (đợt chạy thử: 27,12%) | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ mỗi việc ở 45.000 yêu cầu/tháng (4.599 đ = 0,38x), +2.370 đ nếu còn một nửa (5.784 đ = 0,48x) [simulated] | Số việc thành công theo tuần dưới 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
| Giữ 3 lần chạy thay vì 2 | Cả hệ thống đắt hơn 136.365 đ trên 1.200 yêu cầu mẫu (7.037.585 đ so với 6.901.220 đ, toàn mẫu gồm cả quoc_te, nơi ok lần 3 chỉ 2,2%) [simulated] | Tỉ lệ ok ở lần chạy thứ 3 của hang_nang dưới 20% (đợt chạy thử: 17,9%; noi_dia: 38,9%) | Đặt giới hạn 2 lần chạy cho hang_nang, giữ 3 lần cho noi_dia nếu tỉ lệ ok lần 3 còn trên 30% | Kỹ sư trưởng agent |
