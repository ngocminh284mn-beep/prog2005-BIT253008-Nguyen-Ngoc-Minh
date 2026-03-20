class SinhVien:
    truong = "Đại học CMC"

    def __init__(self, ten, diem):
        if diem < 0:
            raise ValueError("Lỗi: Điểm không được nhỏ hơn 0!")
        self.ten = ten
        self._tuoi = 18
        self.diem = diem
    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, gia_tri):
        if gia_tri < 18:
            raise ValueError("Lỗi: Tuổi sinh viên phải >= 18")
        self._tuoi = gia_tri
    def __str__(self):
        return f"Tên: {self.ten} | Tuổi: {self.tuoi} | Điểm: {self.diem}"
    def __eq__(self, other):
        return self.diem == other.diem
    def hoc_bai(self):
        return f"{self.ten} đang học bài."
    @classmethod
    def doi_ten_truong(cls, ten_moi):
        cls.truong = ten_moi
    @staticmethod
    def thong_bao():
        return "Xin chào từ hệ thống trường học."
class LopTruong(SinhVien):
    def __init__(self, ten, diem, chuc_vu):
        super().__init__(ten, diem)
        self.chuc_vu = chuc_vu

    def __str__(self):
        return super().__str__() + f" | Chức vụ: {self.chuc_vu}"
def bai_9():
    print("\n--- BÀI 9: VÍ DỤ CLASS OOP ---")
    try:
        sv1 = SinhVien("An", 8.0)
        sv2 = SinhVien("Bình", 8.0)
        lt = LopTruong("Cường", 9.5, "Lớp trưởng")

        print(sv1)
        print(lt)
        print(f"An và Bình có bằng điểm nhau không? -> {sv1 == sv2}")
        print(sv1.hoc_bai())
        SinhVien.doi_ten_truong("Đại học CMC")
        print(f"Trường hiện tại: {SinhVien.truong}")
        print(SinhVien.thong_bao())
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    bai_9()