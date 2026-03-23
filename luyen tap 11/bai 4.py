import math
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True
my_list = [5, 2, 9, 1, 5, 6, 7]
print("1. Danh sách ban đầu:", my_list)
my_list.append(10)
print("2. Danh sách sau khi thêm '10':", my_list)
k = int(input("3. Nhập giá trị k cần đếm số lần xuất hiện: "))
so_lan = my_list.count(k)
print(f" => Số {k} xuất hiện {so_lan} lần trong danh sách.")
tong_nguyen_to = sum(x for x in my_list if is_prime(x))
print(f"4. Tổng các số nguyên tố trong danh sách là: {tong_nguyen_to}")
my_list.sort()
print("5. Danh sách sau khi sắp xếp tăng dần:", my_list)
my_list.clear()
print("6. Danh sách sau khi xóa:", my_list)