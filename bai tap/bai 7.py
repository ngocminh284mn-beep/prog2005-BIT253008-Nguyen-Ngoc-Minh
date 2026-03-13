class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
sv1 = Student("Nguyen Ngoc Minh", 10)
sv2 = Student("Nguyen Van Dat", 9)
print("Đã tạo sinh viên 1:", sv1.ten, "- Điểm:", sv1.diem)
print("Đã tạo sinh viên 2:", sv2.ten, "- Điểm:", sv2.diem)