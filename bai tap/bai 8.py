class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        if diem >= 0 and diem <= 10:
            self.diem = diem
            print("Nhập điểm thành công cho", self.ten)
        else:
            print("Lỗi: Điểm của", self.ten, "không hợp lệ! (Phải từ 0-10)")
            self.diem = 0  # Gán tạm bằng 0 nếu nhập sai
sv_hop_le = Student("Le Van Duc", 7)  # Điểm hợp lệ
sv_khong_hop_le = Student("Nguyen Ngoc Minh", 10)  # Điểm 12 sẽ bị báo lỗi