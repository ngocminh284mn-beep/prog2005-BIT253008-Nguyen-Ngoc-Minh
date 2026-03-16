chuoi = input("Nhập vào một chuỗi: ")

in_hoa = 0
in_thuong = 0
chu_so = 0
dac_biet = 0
khoang_trang = 0
nguyen_am = 0
phu_am = 0
cac_nguyen_am = "aeiouAEIOU"

for ky_tu in chuoi:
    if ky_tu.isupper():
        in_hoa += 1
    elif ky_tu.islower():
        in_thuong += 1
    if ky_tu.isdigit():
        chu_so += 1
    elif ky_tu.isspace():
        khoang_trang += 1
    elif not ky_tu.isalpha():
        dac_biet += 1
    if ky_tu.isalpha():
        if ky_tu in cac_nguyen_am:
            nguyen_am += 1
        else:
            phu_am += 1

print("\n--- Kết quả thống kê ---")
print(f"- Số lượng chữ cái in hoa: {in_hoa}")
print(f"- Số lượng chữ cái in thường: {in_thuong}")
print(f"- Số lượng chữ số: {chu_so}")
print(f"- Số lượng ký tự đặc biệt: {dac_biet}")
print(f"- Số lượng ký tự khoảng trắng: {khoang_trang}")
print(f"- Số lượng nguyên âm: {nguyen_am}")
print(f"- Số lượng phụ âm: {phu_am}")