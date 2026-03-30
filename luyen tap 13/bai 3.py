i = 1
tong_so_le = 0
print("Các số lẻ từ 1 đến 30 là:")
while i <= 30:
    if i % 2 != 0:
        print(i, end=" ")
        tong_so_le += i
    i += 1
print("\nTổng của tất cả các số lẻ này là:", tong_so_le)