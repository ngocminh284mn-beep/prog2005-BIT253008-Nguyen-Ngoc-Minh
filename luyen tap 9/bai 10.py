class SinhVien:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
    def __eq__(self, other):
        if isinstance(other, SinhVien):
            return self.diem == other.diem
        return False

print("Thong tin sinh vien 1:")
ten1 = input("ten sinh vien: ")
diem1 = float(input("diem sinh vien: "))
sv1 = SinhVien(ten1, diem1)
print("\nThong tin sinh vien 2:")
ten2 = input("Tên: ")
diem2 = float(input("Điểm: "))
sv2 = SinhVien(ten2, diem2)

print("\n Kết quả so sánh")
if sv1 == sv2:
    print(f"Hai sinh viên {sv1.ten} và {sv2.ten} diem bang nhau ({sv1.diem}).")
else:
    print(f"Hai sinh viên {sv1.ten} và {sv2.ten} khac diem nhau .")