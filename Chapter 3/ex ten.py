user_list = [int(x) for x in input("Nhập các số nguyên: ").split()]
total_even = 0

print("Các số chẵn trong danh sách:")
for num in user_list:
    if num % 2 == 0:
        print(num)
        total_even += num

print("Tổng các số chẵn là:", total_even)