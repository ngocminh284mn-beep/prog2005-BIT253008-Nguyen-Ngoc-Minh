def lay_ten_file_co_duoi(duong_dan):
    duong_dan = duong_dan.strip('"\' ')
    duong_dan = duong_dan.replace('\\', '/')
    ten_file = duong_dan.split('/')[-1]
    return ten_file
def lay_ten_file_khong_duoi(duong_dan):
    ten_file_co_duoi = lay_ten_file_co_duoi(duong_dan)
    if '.' in ten_file_co_duoi:
        ten_khong_duoi = ten_file_co_duoi.rsplit('.', 1)[0]
        return ten_khong_duoi

    return ten_file_co_duoi
def bai_1():
    print("\n--- BÀI 1: TRÍCH XUẤT TÊN BÀI HÁT ---")
    duong_dan = input("Nhập đường dẫn bài hát (VD: d:\\music\\muabui.mp3): ")
    print(f"-> Kết quả 1 (Có đuôi): {lay_ten_file_co_duoi(duong_dan)}")
    print(f"-> Kết quả 2 (Không đuôi): {lay_ten_file_khong_duoi(duong_dan)}")
if __name__ == "__main__":
    bai_1()