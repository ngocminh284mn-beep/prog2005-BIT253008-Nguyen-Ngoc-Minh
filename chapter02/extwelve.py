n = int(input("Nhập n: "))
tong_le = 0

# Cách 1: Duyệt từng số và kiểm tra lẻ
for i in range(1, n + 1):
    if i % 2 != 0:  # Nếu chia 2 dư khác 0 là số lẻ
        tong_le += i

print(f"Tổng các số lẻ từ 1 đến {n} là: {tong_le}")