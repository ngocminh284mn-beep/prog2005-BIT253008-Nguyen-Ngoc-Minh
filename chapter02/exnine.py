n = input("Nhập số có 5 chữ số: ")
max_val = n[0]
for chu_so in n:
    if chu_so > max_val:
        max_val = chu_so
print(f"Chữ số lớn nhất: {max_val}")