while True:
    try:
        so = int(input("Vui lòng nhập một số từ 1 đến 9: "))
        if 1 <= so <= 9:
            break
        else:
            print("Số bạn nhập không nằm trong khoảng từ 1 đến 9. Hãy thử lại.\n")
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.\n")
print(f"\n--- BẢNG CỬU CHƯƠNG {so} ---")
for i in range(1, 10):
    ket_qua = so * i
    print(f"{so} x {i} = {ket_qua}")