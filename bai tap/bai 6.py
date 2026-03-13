import math

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
chuoi = " 5; 7; 8; -2; 8; 11; 13; 9; 10 "
danh_sach_chuoi = chuoi.split(";")
mang_so = []
for s in danh_sach_chuoi:
    so = int(s.strip())
    mang_so.append(so)
print("--- Các số trong chuỗi ---")
for so in mang_so:
    print(so)
dem_chan = 0
dem_am = 0
dem_nguyen_to = 0
tong = 0
for so in mang_so:
    if so % 2 == 0:
        dem_chan += 1

    if so < 0:
        dem_am += 1

    if kiem_tra_nguyen_to(so):
        dem_nguyen_to += 1


    tong += so


trung_binh = tong / len(mang_so)

print("--- Kết quả thống kê ---")
print("Số lượng số chẵn:", dem_chan)
print("Số lượng số âm:", dem_am)
print("Số lượng số nguyên tố:", dem_nguyen_to)
print("Giá trị trung bình:", trung_binh)