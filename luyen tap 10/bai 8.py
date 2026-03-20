def bai_8():
    print("\n--- BÀI 8: SẮP XẾP 5 CHUỖI GIẢM DẦN ---")
    danh_sach = []
    for i in range(5):
        chuoi = input(f"Nhập chuỗi thứ {i + 1}: ")
        danh_sach.append(chuoi)
    n = len(danh_sach)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if len(danh_sach[j]) < len(danh_sach[j + 1]):
                danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]

        print(f"Bước {i + 1}: {danh_sach}")

if __name__ == "__main__":
    bai_8()