s = input("Nhập chuỗi: ")
char = input("Nhập ký tự: ")
count = 0
for c in s:
    if c == char:
        count += 1
print(f"Số lần xuất hiện: {count}")