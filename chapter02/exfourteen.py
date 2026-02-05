n = int(input("Nhập số cần kiểm tra: "))

if n < 2:
    print(f"{n} không phải là số nguyên tố")
else:
    la_nguyen_to = True
    # Chỉ cần kiểm tra từ 2 đến căn bậc 2 của n để tối ưu
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_nguyen_to = False
            break  # Thoát vòng lặp ngay khi tìm thấy ước số

    if la_nguyen_to:
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")