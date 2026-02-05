n = int(input("Nhập n: "))
kq = 1
for i in range(2, n + 1):
    kq *= i
print(f"Giai thừa: {kq}")