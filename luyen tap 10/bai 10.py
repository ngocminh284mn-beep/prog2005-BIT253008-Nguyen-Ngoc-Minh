def bai_10():
    print("\n--- BÀI 10: BUBBLE SORT VỚI CHUỖI ---")
    mang_chuoi = []

    for i in range(5):
        mang_chuoi.append(input(f"Mời nhập chuỗi {i + 1}: "))

    so_luong = len(mang_chuoi)
    for i in range(so_luong - 1):
        for j in range(so_luong - 1 - i):
            if len(mang_chuoi[j]) < len(mang_chuoi[j + 1]):
                mang_chuoi[j], mang_chuoi[j + 1] = mang_chuoi[j + 1], mang_chuoi[j]

        print(f"Trạng thái mảng ở bước {i + 1}: {mang_chuoi}")
if __name__ == "__main__":
    bai_10()