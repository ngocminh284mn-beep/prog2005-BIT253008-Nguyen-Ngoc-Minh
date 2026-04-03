import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
nhap_mang = input("Nhập mảng các số tự nhiên (cách nhau bởi dấu cách): ")
mang = [int(x) for x in nhap_mang.split()]
so_le = [x for x in mang if x % 2 != 0]
so_nguyen_to = [x for x in mang if is_prime(x)]
print(f"Dòng 1: Các số lẻ: {so_le} - Tổng số lượng số lẻ: {len(so_le)}")
print(f"Dòng 2: Các số nguyên tố: {so_nguyen_to}")