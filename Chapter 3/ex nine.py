user_list = [int(x) for x in input("Nhập các số nguyên: ").split()]

print("Các số lẻ trong danh sách:")
for num in user_list:
    if num % 2 != 0:
        print(num)