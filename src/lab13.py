"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.

Cấu trúc: A1 (ba phép thử) · A2 (mo_hinh) · A3 (theo loại) · A4 (chi phí cố định)
          B1–B4 (độ nhạy) · D1 (cỡ mẫu) · E1 (ba chỉ số tính thử).
Mọi số tính từ cột *_simulated được in kèm nhãn [simulated].
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)

CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý, đồng/tháng
KHOI_LUONG_THANG = 45_000    # yêu cầu hoàn phí mỗi tháng (1.500 / ngày)
PHAM_VI = ['noi_dia', 'hang_nang']   # phạm vi pilot (kết luận từ A3)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP (simulated).
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B; giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]   # chỉ lấy lần chạy của các yêu cầu đang xét
    if max_lan_chay is not None:                               # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay              # chạy quá giới hạn → nhân viên làm thay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


# ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
def bang_theo_loai(runs, reqs):
    """Một dòng cho mỗi giá trị của cột loai."""
    dong = []
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        m = mo_hinh(runs, reqs[reqs.loai == loai])
        so_run = runs['request_id'].isin(r['request_id']).sum()
        dong.append(dict(loai=loai, so_yc=len(r), ti_le_tc=m['thanh_cong'] / len(r),
                         run_moi_yc=so_run / len(r), cps=m['cps'], so_voi_12k=m['cps'] / BASELINE))
    return pd.DataFrame(dong)


def ti_le_ok_theo_lan_thu(runs, reqs):
    """Tỉ lệ ok theo loại và lần thử: trả lời 'chạy lại có giúp không'."""
    m = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    m['ok'] = (m['status'] == 'ok').astype(float)
    return m.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')


# ---------- Nhiệm vụ A4 · Chi phí cố định ----------
def chi_phi_co_dinh(runs, reqs, he_so_khoi_luong=1.0):
    """Cộng chi phí cố định 40 triệu/tháng vào chi phí mỗi việc thành công của phạm vi pilot."""
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    m = mo_hinh(runs, pv)
    viec_thang = KHOI_LUONG_THANG * he_so_khoi_luong * m['thanh_cong'] / len(reqs)
    co_dinh_moi_viec = CO_DINH_THANG / viec_thang
    cps = m['cps'] + co_dinh_moi_viec
    return dict(viec_thang=viec_thang, co_dinh=co_dinh_moi_viec, cps_pv=m['cps'],
                cps=cps, so_voi_12k=cps / BASELINE)


def chi_phi_he_thong(runs, reqs, **kw):
    """Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay)."""
    m = mo_hinh(runs, reqs, **kw)
    khong_tc = len(reqs) - m['thanh_cong']
    return dict(tong_tro_ly=m['tong'], khong_tc=khong_tc,
                he_thong=m['tong'] + BASELINE * khong_tc, cps=m['cps'])


# ---------- Nhiệm vụ B · Độ nhạy ----------
KICH_BAN = {
    'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
    'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
    'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
    'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
    'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
    'Lương tăng 25%':           dict(luong_phut=2500),
    'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
    'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
}


def xem_lai_tat_ca(runs, reqs, phut_xem=5, phut_lam_lai=9):
    """B4: mọi yêu cầu có ít nhất một lần chạy ok đều phải xem lại (mặc định 5 phút), ca lam_lai mất 9 phút làm lại.
    Chỉ tính phạm vi noi_dia + hang_nang. Các phút này là giả định đề bài → simulated."""
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    r = runs[runs['request_id'].isin(pv['request_id'])]
    so_xem = r[r['status'] == 'ok']['request_id'].nunique()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    token_tool = ((r['tokens_in'] / 1000 * GIA_VAO + r['tokens_out'] / 1000 * GIA_RA)
                  + r['tool_calls'] * GIA_TOOL).sum()
    tien_xem = so_xem * phut_xem * LUONG_PHUT
    tien_lam = so_lam_lai * phut_lam_lai * LUONG_PHUT
    tong = token_tool + tien_xem + tien_lam
    thanh_cong = int((pv['ket_qua'] == 'thanh_cong').sum())
    return dict(so_xem=so_xem, so_lam_lai=so_lam_lai, token_tool=token_tool, tien_xem=tien_xem,
                tien_lam=tien_lam, tong=tong, thanh_cong=thanh_cong,
                cps=tong / thanh_cong, so_voi_12k=tong / thanh_cong / BASELINE,
                hoa_von_phut_xem=(thanh_cong * BASELINE - token_tool - tien_lam) / so_xem / LUONG_PHUT)


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ, chia theo yêu cầu (độc lập)."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc):
    return 1 + (m - 1) * icc


def m_toi_thieu(c, icc, n_can):
    """Số yêu cầu tối thiểu mỗi cụm để c cụm đạt cỡ mẫu hiệu dụng n_can: c·m / (1+(m-1)icc) >= n_can."""
    return math.ceil(n_can * (1 - icc) / (c - n_can * icc))


# ---------- Nhiệm vụ E1 · Ba chỉ số tính thử ----------
def chi_so_thu(reqs):
    chinh = ((reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0))
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    return dict(chinh=chinh.mean(), chinh_n=int(chinh.sum()),
                bo_qua=bo_qua.mean(), bo_qua_n=int(bo_qua.sum()), duoc_xem=len(xem),
                an_toan=(reqs.mo_lai_trong_7_ngay == 1).mean(),
                an_toan_n=int((reqs.mo_lai_trong_7_ngay == 1).sum()))


def tieu_de(s):
    print(f'\n=== {s} ===')


if __name__ == '__main__':
    import sys
    if hasattr(sys.stdout, 'reconfigure'):          # console Windows mặc định cp1252 không in được tiếng Việt
        sys.stdout.reconfigure(encoding='utf-8')
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)   # bắt buộc keep_default_na=False

    # ---------------- CP1 · A ----------------
    tieu_de('A1 · ba phép thử')
    kiem_tra_dap_an_biet_truoc()
    print(f'  so_lan_chay_ky_vong(0.8, 2)   = {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  so_lan_chay_ky_vong(0.8)      = {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  he_so_chi_phi(0.8, 3)         = {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    tieu_de('A2 · mô hình chi phí từ trace (xem_lai, lam_lai, tong, cps: simulated)')
    goc = mo_hinh(runs, reqs)
    for ten, gia_tri in goc.items():
        print(f'  {ten:16s} {gia_tri:>14,.1f}')
    tong = goc['tong']
    print(f"  cps / hoa_don_moi_yc = {goc['cps'] / goc['hoa_don_moi_yc']:.1f} lần")
    print(f"  tỉ trọng: làm lại {goc['lam_lai'] / tong:.1%} · xem lại {goc['xem_lai'] / tong:.1%} "
          f"· giờ nhân viên {(goc['lam_lai'] + goc['xem_lai']) / tong:.1%} [simulated]")
    he_thong = chi_phi_he_thong(runs, reqs)
    moi_yc = (he_thong['he_thong']) / len(reqs)
    print(f"  cả hệ thống / yêu cầu = {moi_yc:,.0f} đ = {moi_yc / BASELINE:.2f}× của 12.000 đ "
          f"(đã cộng {he_thong['khong_tc']} ca nhân viên làm thay) [simulated]")

    tieu_de('A3 · theo loại yêu cầu [simulated]')
    a3 = bang_theo_loai(runs, reqs)
    print(a3.to_string(index=False, formatters={
        'ti_le_tc': '{:.1%}'.format, 'run_moi_yc': '{:.2f}'.format,
        'cps': '{:,.0f}'.format, 'so_voi_12k': '{:.2f}x'.format}))
    print('  Tỉ lệ ok theo lần thử:')
    print(ti_le_ok_theo_lan_thu(runs, reqs).round(3).to_string())

    tieu_de('A4 · chi phí cố định, phạm vi noi_dia + hang_nang [simulated]')
    for ten, hs in [('45.000 yc/tháng', 1.0), ('một nửa khối lượng', 0.5)]:
        a4 = chi_phi_co_dinh(runs, reqs, hs)
        print(f"  {ten:20s} việc thành công/tháng {a4['viec_thang']:>8,.0f} · cố định/việc {a4['co_dinh']:>6,.0f} đ "
              f"· cps trong phạm vi {a4['cps_pv']:,.0f} → +cố định {a4['cps']:,.0f} đ = {a4['so_voi_12k']:.2f}×")

    # ---------------- CP2 · B ----------------
    tieu_de('B1 · đổi từng yếu tố [simulated]')
    g = goc['cps']
    print(f"  {'Gốc (A2)':26s} {g:8,.0f}")
    ket_qua_b1 = {}
    for ten, kw in KICH_BAN.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        ket_qua_b1[ten] = cps
        print(f'  {ten:26s} {cps:8,.0f} {(cps / g - 1) * 100:+6.1f}%')
    # Tự kiểm tra: "giảm một nửa" phải bằng đúng nửa mức tăng của "gấp đôi"
    for dôi, nua in [('Giá token gấp đôi', 'Giá token giảm một nửa'),
                     ('Xem lại gấp đôi', 'Xem lại giảm một nửa'),
                     ('Làm lại gấp đôi', 'Làm lại giảm một nửa')]:
        tang, giam = ket_qua_b1[dôi] / g - 1, 1 - ket_qua_b1[nua] / g
        assert abs(tang / 2 - giam) < 1e-9, f'{nua}: không bằng nửa mức tăng của {dôi}'
    print('  Tự kiểm tra "giảm một nửa = nửa mức tăng": ĐẠT')

    tieu_de('B2 · đổi một cặp và xếp hạng [simulated]')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'  Giá token ×2 + xem lại ×2: {cap:,.0f} đ ({(cap / g - 1) * 100:+.1f}%)')
    tac_dong = {k: abs(ket_qua_b1[k] / g - 1) for k in
                ['Giá token gấp đôi', 'Xem lại gấp đôi', 'Làm lại gấp đôi', 'Lương tăng 25%']}
    for i, (k, v) in enumerate(sorted(tac_dong.items(), key=lambda kv: -kv[1]), 1):
        print(f'  {i}. {k:22s} {v:.1%}')

    tieu_de('B3 · giới hạn chạy lại và chi phí cả hệ thống [simulated]')
    print(f"  {'Giới hạn':9s} {'Tổng trợ lý':>12s} {'Không thành công':>17s} {'Cả hệ thống':>12s} {'cps':>7s}")
    for k in (1, 2, 3):
        b3 = chi_phi_he_thong(runs, reqs, max_lan_chay=k)
        print(f"  {k} lần{'':4s} {b3['tong_tro_ly']:>12,.0f} {b3['khong_tc']:>17d} "
              f"{b3['he_thong']:>12,.0f} {b3['cps']:>7,.0f}")

    tieu_de('B4 · xem lại 100%, noi_dia + hang_nang [simulated]')
    for ten, pl in [('làm lại 9 phút (đề bài)', 9), ('làm lại 15,3 phút (đúng dữ liệu)', None)]:
        if pl is None:
            lam = reqs[reqs.ket_qua == 'lam_lai']['phut_lam_lai_simulated']   # toàn bộ ca lam_lai của mẫu
            pl = lam.mean()
            print(f'  Phút làm lại trung bình trên toàn bộ {len(lam)} ca lam_lai: {pl:.1f} (trung vị {lam.median():.1f}) [simulated]')
            lam_pv = reqs[(reqs.loai.isin(PHAM_VI)) & (reqs.ket_qua == 'lam_lai')]['phut_lam_lai_simulated']
            print(f'  (Ghi chú: riêng phạm vi noi_dia + hang_nang, {len(lam_pv)} ca: {lam_pv.mean():.1f} phút)')
        b4 = xem_lai_tat_ca(runs, reqs, phut_lam_lai=pl)
        print(f"  {ten:34s} xem {b4['so_xem']} yc · lam_lai {b4['so_lam_lai']} ca · token+tool {b4['token_tool']:,.0f} "
              f"· tổng {b4['tong']:,.0f} · cps {b4['cps']:,.0f} đ = {b4['so_voi_12k']:.2f}× "
              f"· hoà vốn xem lại ≤ {b4['hoa_von_phut_xem']:.1f} phút")

    # ---------------- CP4 · D1 ----------------
    tieu_de('D1 · cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02)')
    ICC = 0.02
    n_a = co_mau(0.70, 0.75)
    print(f'  a) Chia theo yêu cầu: {n_a} yêu cầu mỗi nhóm')
    de_b = he_so_thiet_ke(75, ICC)
    n_b = math.ceil(n_a * de_b)
    print(f'  b) Theo nhân viên, m=75: DE = {de_b:.2f} → {n_b} yêu cầu mỗi nhóm → {math.ceil(n_b / 75)} người mỗi nhóm, '
          f'tổng {2 * math.ceil(n_b / 75)} > 40 nhân viên: không đủ người')
    print(f'  c) 20 nhân viên mỗi nhóm: cỡ mẫu hiệu dụng tối đa 20/ICC = {20 / ICC:,.0f} < {n_a}: không đạt')
    print(f'  d) 6 depot mỗi nhóm: tối đa 6/ICC = {6 / ICC:,.0f}')
    n_e = co_mau(0.70, 0.76)
    m_e = m_toi_thieu(20, ICC, n_e)
    print(f'  e) Chênh 6 điểm: {n_e} mỗi nhóm; 20 người mỗi nhóm cần m ≥ {m_e} yêu cầu/người '
          f'(DE = {he_so_thiet_ke(m_e, ICC):.2f})')
    try:
        from statsmodels.stats.power import NormalIndPower
        from statsmodels.stats.proportion import proportion_effectsize
        es = proportion_effectsize(0.75, 0.70)
        pw = NormalIndPower().power(effect_size=es, nobs1=n_e, alpha=0.05, ratio=1.0)
        print(f'  Nếu chọn mức chênh 6 điểm (n={n_e}/nhóm) mà tác động thật chỉ 5 điểm: power ≈ {pw:.2f}')
    except ImportError:
        print('  (cài statsmodels để tính power)')
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    print(f'  Tỉ lệ mở lại 7 ngày hiện tại: {reqs.mo_lai_trong_7_ngay.mean():.2%} '
          f'({int(reqs.mo_lai_trong_7_ngay.sum())}/{len(reqs)}); trong phạm vi noi_dia + hang_nang: '
          f'{pv.mo_lai_trong_7_ngay.mean():.2%}')
    print(f"  Tỉ lệ làm lại trong phạm vi: {(pv.ket_qua == 'lam_lai').mean():.1%}")

    # ---------------- CP5 · E1 ----------------
    tieu_de('E1 · ba chỉ số tính thử trên 1.200 yêu cầu (đợt chạy thử, không có đối chứng)')
    cs = chi_so_thu(reqs)
    print(f"  Chính  (đóng 24h, không mở lại 7 ngày): {cs['chinh']:.2%} ({cs['chinh_n']}/{len(reqs)})")
    print(f"  Dùng   (bỏ qua gợi ý = sua + bo):        {cs['bo_qua']:.2%} ({cs['bo_qua_n']}/{cs['duoc_xem']})")
    print(f"  An toàn(mở lại trong 7 ngày):            {cs['an_toan']:.2%} ({cs['an_toan_n']}/{len(reqs)})")
