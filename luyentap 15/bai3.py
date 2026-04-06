def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)
num = int(input("Nhập số cần tính giai thừa: "))
print(f"Giai thừa của {num} là: {giai_thua(num)}")