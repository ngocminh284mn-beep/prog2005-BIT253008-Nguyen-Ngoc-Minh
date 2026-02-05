diem = float(input("Nhập điểm trung bình: "))

if diem >= 8.0:
    xep_loai = "Giỏi"
elif 6.5 <= diem < 8.0:
    xep_loai = "Khá"
elif 5.0 <= diem < 6.5:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print(f"Học lực của bạn là: {xep_loai}")