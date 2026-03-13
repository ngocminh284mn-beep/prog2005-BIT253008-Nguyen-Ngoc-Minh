import random
m = int(input("Nhập số lượng hàng M: "))
n = int(input("Nhập số lượng cột N: "))
ma_tran = []
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(random.randint(1, 100))
    ma_tran.append(hang)
print("\n--- MA TRẬN M x N ĐÃ TẠO ---")
for hang in ma_tran:
    print(hang)
hang_can_xem = int(input(f"\nNhập chỉ số hàng bạn muốn xem (từ 0 đến {m-1}): "))
if 0 <= hang_can_xem < m:
    print(f"=> Dữ liệu của hàng {hang_can_xem}: {ma_tran[hang_can_xem]}")
else:
    print("=> Chỉ số hàng bạn nhập không hợp lệ.")
cot_can_xem = int(input(f"\nNhập chỉ số cột bạn muốn xem (từ 0 đến {n-1}): "))
if 0 <= cot_can_xem < n:
    print(f"=> Dữ liệu của cột {cot_can_xem}: ", end="")
    for i in range(m):
        print(ma_tran[i][cot_can_xem], end=" ")
    print()
else:
    print("=> Chỉ số cột bạn nhập không hợp lệ.")
gia_tri_lon_nhat = ma_tran[0][0]
for hang in ma_tran:
    for phan_tu in hang:
        if phan_tu > gia_tri_lon_nhat:
            gia_tri_lon_nhat = phan_tu

print(f"\n--- KẾT QUẢ ---")
print(f"Giá trị lớn nhất trong toàn bộ ma trận là: {gia_tri_lon_nhat}")