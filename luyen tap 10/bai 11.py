import subprocess
import sys
import os


def menu_chinh():
    while True:
        print("\n" + "=" * 45)
        print("    MENU TỔNG HỢP BÀI TẬP PYTHON (1-10)")
        print("=" * 45)
        print("1. Chạy bai 1.py")
        print("2. Chạy bai 2.py")
        print("3. Chạy bai 3.py")
        print("4. Chạy bai 4.py")
        print("5. Chạy bai 5.py")
        print("6. Chạy bai 6.py")
        print("7. Chạy bai 7.py")
        print("8. Chạy bai 8.py")
        print("9. Chạy bai 9.py")
        print("10. Chạy bai 10.py")
        print("0. THOÁT CHƯƠNG TRÌNH")
        print("=" * 45)

        lua_chon = input("Nhập số bài bạn muốn chạy (0-10): ")

        if lua_chon == '0':
            print("Đã thoát chương trình. Chúc bạn học tốt!")
            break
        elif lua_chon.isdigit() and 1 <= int(lua_chon) <= 10:
            ten_file = f"bai {lua_chon}.py"
            if os.path.exists(ten_file):
                print(f"\n{'=' * 15} ĐANG CHẠY {ten_file.upper()} {'=' * 15}\n")
                subprocess.run([sys.executable, ten_file])

                print(f"\n{'=' * 15} KẾT THÚC {ten_file.upper()} {'=' * 15}")
            else:
                print(f"\n[Lỗi] Không tìm thấy file '{ten_file}'. Hãy đảm bảo file này nằm cùng thư mục với bai 11.py!")
        else:
            print("Lựa chọn sai! Vui lòng nhập số từ 0 đến 10.")


if __name__ == "__main__":
    menu_chinh()