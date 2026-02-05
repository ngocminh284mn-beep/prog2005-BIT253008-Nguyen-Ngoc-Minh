mat_khau_dung = "casaulenbo"
mat_khau_nhap = ""

while mat_khau_nhap != mat_khau_dung:
    mat_khau_nhap = input("Vui lòng nhập mật khẩu: ")
    if mat_khau_nhap != mat_khau_dung:
        print("Mật khẩu sai, vui lòng thử lại!")

print("Đăng nhập thành công!")