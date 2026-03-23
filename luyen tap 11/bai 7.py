import csv
ten = input("Nhập tên nhân viên: ")
tuoi = input("Nhập tuổi nhân viên: ")
id_nv = input("Nhập ID nhân viên: ")
with open('thongtin_nhanvien.txt', 'a', encoding='utf-8') as f_txt:
    f_txt.write(f"ID: {id_nv}, Tên: {ten}, Tuổi: {tuoi}\n")
print("Đã lưu thông tin vào file 'thongtin_nhanvien.txt'.")
with open('thongtin_nhanvien.csv', 'a', newline='', encoding='utf-8') as f_csv:
    writer = csv.writer(f_csv)
    writer.writerow([id_nv, ten, tuoi])
print("Đã lưu thông tin vào file 'thongtin_nhanvien.csv'.")