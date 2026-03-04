s = input("Nhập chuỗi cần đảo ngược: ")

# Cách 1: Sử dụng Slicing
rev_slicing = s[::-1]
print("Đảo ngược bằng Slicing:", rev_slicing)

# Cách 2: Không sử dụng Slicing (dùng vòng lặp)
rev_no_slicing = ""
for char in s:
    rev_no_slicing = char + rev_no_slicing

print("Đảo ngược không dùng Slicing:", rev_no_slicing)