so_nhap_vao = input("Nhập vào một số: ")
tong = 0
for chu_so in so_nhap_vao:
    if chu_so.isdigit():
        tong += int(chu_so)

print(f"Tổng các chữ số của {so_nhap_vao} là: {tong}")