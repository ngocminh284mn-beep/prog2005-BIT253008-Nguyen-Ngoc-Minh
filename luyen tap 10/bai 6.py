chuoi = input("Nhập chuỗi cần đảo ngược: ")
chuoi_dao_nguoc = ""
for ky_tu in chuoi:
    chuoi_dao_nguoc = ky_tu + chuoi_dao_nguoc
print(f"Chuỗi sau khi đảo ngược là: {chuoi_dao_nguoc}")