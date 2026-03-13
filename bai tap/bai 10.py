def nhap_va_luu_san_pham():
    print("--- Nhập thông tin sản phẩm ---")
    code = input("Nhập mã sản phẩm (Code): ")
    name = input("Nhập tên sản phẩm (Name): ")
    price = float(input("Nhập giá (Price): "))
    with open("sanpham.txt", "a", encoding="utf-8") as file:
        file.write(f"{code}, {name}, {price}\n")

    print("-> Đã lưu thành công vào file 'sanpham.txt'")

nhap_va_luu_san_pham()