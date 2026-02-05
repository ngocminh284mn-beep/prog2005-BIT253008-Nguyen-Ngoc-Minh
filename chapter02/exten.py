def sum_recursive(n):
    return n + sum_recursive(n - 1) if n > 0 else 0

n = int(input("Nhập n: "))
print(f"Tổng: {sum_recursive(n)}")