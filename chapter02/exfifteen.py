n = int(input("Nhập một số nguyên dương: "))
temp = n  # Lưu lại giá trị n để in ra sau này nếu cần
tong = 0

while n > 0:
    chu_so = n % 10  # Lấy chữ số cuối cùng
    tong += chu_so   # Cộng vào tổng
    n = n // 10      # Bỏ chữ số cuối cùng đi

print(f"Tổng các chữ số của {temp} là: {tong}")