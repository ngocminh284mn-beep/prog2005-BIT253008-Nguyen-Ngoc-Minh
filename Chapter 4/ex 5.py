class Product:
    def __init__(self, price):
        self._price = 0
        self.set_price(price)
    def get_price(self):
        return self._price
    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print(f"Lỗi: Giá nhập vào ({price}) không hợp lệ. Giá phải > 0!")
    def __str__(self):
        return f"Giá của sản phẩm là: {self._price}"

print("\n--- Bài 5 ---")
sp_hop_le = Product(50000)
print(sp_hop_le)
sp_loi = Product(-100)
print(sp_loi)