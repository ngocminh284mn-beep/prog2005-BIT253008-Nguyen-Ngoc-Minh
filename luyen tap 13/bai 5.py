class Flower:
    def __init__(self):
        self._color = ""
    def get_color(self):
        return self._color
    def set_color(self, color):
        self._color = color
hoa_hong = Flower()
hoa_hong.set_color("Màu đỏ")
print("Thuộc tính color của đối tượng là:", hoa_hong.get_color())