def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * tinh_giai_thua(n - 1)
so = int(input("Nhập vào một số nguyên dương: "))
if so < 0:
    print("Không có giai thừa cho số âm!")
else:
    print(f"Giai thừa của {so} là: {tinh_giai_thua(so)}")