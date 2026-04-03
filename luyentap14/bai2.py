danh_sach_ten = []
print("Nhập tên 5 người:")
for i in range(5):
    ten = input(f"Người thứ {i+1}: ")
    danh_sach_ten.append(ten)
print("\nDanh sách sau khi nhập:", danh_sach_ten)
if len(danh_sach_ten) >= 2:
    del danh_sach_ten[1]
print("Danh sách sau khi xóa :", danh_sach_ten)