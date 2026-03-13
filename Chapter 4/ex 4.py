class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
    def __str__(self):
        return f"Tên hoa: {self.ten} - Màu sắc: {self.mau}"

print("\n--- Bài 4 ---")
hoa_hong = Hoa("Hoa Hồng", "Đỏ")
print(hoa_hong)