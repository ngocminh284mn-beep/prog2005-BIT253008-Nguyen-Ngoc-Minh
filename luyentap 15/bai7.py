students = {"minh": 8.5, "tuan": 7.0, "hoang": 9.0}

def tinh_trung_binh(danh_sach):
    if not danh_sach: return 0
    tong_diem = sum(danh_sach.values())
    return tong_diem / len(danh_sach)

print(f"Điểm trung bình của sinh viên: {tinh_trung_binh(students):.2f}")