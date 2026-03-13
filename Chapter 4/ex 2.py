def tinh_diem_trung_binh(danh_sach_sv):
    tong_diem = sum(danh_sach_sv.values())
    so_luong_sv = len(danh_sach_sv)
    if so_luong_sv == 0:
        return 0

    diem_tb = tong_diem / so_luong_sv
    return diem_tb

sinh_vien = {
    "Nguyễn Văn A": 8.5,
    "Trần Thị B": 2.0,
    "Lê Văn C": 9.0
}

print("\n--- Bài 2 ---")
print("Điểm trung bình của lớp là:", tinh_diem_trung_binh(sinh_vien))