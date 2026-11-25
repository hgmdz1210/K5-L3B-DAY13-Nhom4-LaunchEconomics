# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Nhóm 4 (L3B)
- Nhóm được chấm: AAA (L3B)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện khớp số của nhóm. Nêu số bất lợi: power 0,64 nếu tác động thật là 5 điểm, cỡ mẫu hiệu dụng tối đa 1.000 < 1.251, xem lại 100% = 0,98×–1,03×. Cách xử lý: 4 điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Các số chi phí đều gắn simulated (4.472 đ, 5.865 đ, 11.743 đ). Phạm vi thu hẹp về noi_dia + hang_nang, lý do bằng số: quoc_te 1,88× và thành công 27,3%, doi_tac 0,85×. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Có đối chứng chạy cùng thời gian, chia ngẫu nhiên theo nhân viên, 20 cụm mỗi nhóm, n = 859, DE = 6,96. 3 luật dừng có ngưỡng, thời hạn, người có quyền dừng; rollback 30 phút. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Khớp đề xuất của nhóm AAA. Số liệu nhất quán giữa các file (4.472 đ mỗi việc thành công, 0,49× cả hệ thống, n = 859), nêu rõ số bất lợi (power 0,64; xem lại 100% = 0,98×–1,03×) và có điều kiện kèm người phụ trách và ngày kiểm tra. Điểm cần làm rõ: luật dừng an toàn đo tỉ lệ mở lại 7 ngày nhưng cho dừng sau 3 ngày liên tiếp.

**Một câu hỏi cho đội trình:** Luật dừng an toàn đo tỉ lệ mở lại trong 7 ngày nhưng cho tắt trợ lý sau 3 ngày liên tiếp. Ở bước 0.10 chỉ có khoảng 4 nhân viên: trong 3 ngày đầu, nhóm dựa vào dữ liệu nào để quyết định tắt, khi phần lớn yêu cầu chưa đủ 7 ngày để biết có mở lại hay không?

**Câu trả lời của đội trình (ghi lại tại buổi):** Trong 3 ngày đầu, nhóm dựa vào chỉ báo sớm quan sát được ngay: ca hoàn tiền trùng và lệch sổ cái, vì luật của nhóm có vế "≥ 1 ca hoàn trùng". Tỉ lệ mở lại 7 ngày thì chấm theo tuần, có độ trễ, và chỉ dùng để quyết định chuyển bước rollout. Nhóm thừa nhận ở bước 0.10 chỉ có khoảng 4 nhân viên nên số yêu cầu ít, ngưỡng "+2 điểm" khó phân biệt nhiễu, và có thể giữ trần tuyệt đối 6% hoặc kéo dài quan sát.
