def chuẩn_hoá_tên(name):
    cac_tu = name.split()
    tên_tạm_thời = " ".join(cac_tu)
    tên_chuẩn_hoá = tên_tạm_thời.title()
    return tên_chuẩn_hoá
input_name = input("Nhập tên : ")
result = chuẩn_hoá_tên(input_name)
print(f"Trước: '{input_name}'")
print(f"Sau:  '{result}'")