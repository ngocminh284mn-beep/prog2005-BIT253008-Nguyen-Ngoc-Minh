def tinh_tong_de_quy(n):
    if n <= 1:
        return n
    return n + tinh_tong_de_quy(n - 1)
so_n = int(input("Nhập số n: "))
if so_n < 1:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")
else:
    tong = tinh_tong_de_quy(so_n)
    print(f"Tổng từ 1 đến {so_n} là: {tong}")