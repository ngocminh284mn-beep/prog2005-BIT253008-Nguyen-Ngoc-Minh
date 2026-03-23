danh_sach_nhap = input("Nhập các số, cách nhau bằng dấu phẩy: ")
danh_sach_so = [int(x.strip()) for x in danh_sach_nhap.split(',')]
so_chan = [x for x in danh_sach_so if x % 2 == 0]
tong_chan = sum(so_chan)
print(f"Các số chẵn trong danh sách là: {so_chan}")
print(f"Tổng của các số chẵn đó là: {tong_chan}")