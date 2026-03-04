user_list = [float(x) for x in input("Nhập các số: ").split()]

for num in user_list:
    if num > 10:
        print("Số đầu tiên lớn hơn 10 là:", num)
        break
else:
    print("Không có số nào lớn hơn 10.")