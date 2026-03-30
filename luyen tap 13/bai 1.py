n = int(input("Nhập một số: "))
if n < 0:
    print("Lỗi: Số nhập vào là số âm!")
else:
    phan_du = n % 2
    print(f"Phần dư của {n} khi chia cho 2 là: {phan_du}")