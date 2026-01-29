# Sử dụng vòng lặp để nhập cho 3 người
for i in range(3):
    print(f"\n--- Nhập thông tin sinh viên thứ {i + 1} ---")
    ten = input("Tên sinh viên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))

    dtb = (toan + ly + hoa) / 3
    print(f"Sinh viên {ten} có điểm trung bình: {dtb:.2f}")