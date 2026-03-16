class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Lỗi: Giá trị truyền vào phải lớn hơn 0. Đang thiết lập giá mặc định là 1.")
            self._price = 1

    def __str__(self):
        return f"Thông tin sản phẩm - Giá: {self.price}VND"
san_pham = Product(150000)
print(san_pham)
