def xu_ly_tuple(du_lieu):
    tong = sum(du_lieu)
    gia_tri_lon_nhat = max(du_lieu)
    gia_tri_nho_nhat = min(du_lieu)

    return tong, gia_tri_lon_nhat, gia_tri_nho_nhat
my_tuple = (5, 10, 2, 8)
tong, max_val, min_val = xu_ly_tuple(my_tuple)

print("--- Bài 1 ---")
print("Tổng:", tong)
print("Lớn nhất:", max_val)
print("Nhỏ nhất:", min_val)