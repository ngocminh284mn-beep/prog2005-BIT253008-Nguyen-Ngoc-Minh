def check_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Nhập số: "))
print("Là số nguyên tố" if check_prime(num) else "Không phải số nguyên tố")