danh_sach_sach = [
    ("SGK", 50000),
]
with open("books.txt", "w", encoding="utf-8") as file:
    for name, price in danh_sach_sach:
        file.write(f"{name};{price}\n")

print("Đã lưu thông tin sách vào file 'books.txt' thành công!")