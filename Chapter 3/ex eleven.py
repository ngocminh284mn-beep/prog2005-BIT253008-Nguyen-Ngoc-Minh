arr = [4, 7, 1, 9, -3, 5, 20]
max_val = arr[0]
min_val = arr[0]

for num in arr[1:]:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print(f"Giá trị lớn nhất: {max_val}")
print(f"Giá trị nhỏ nhất: {min_val}")