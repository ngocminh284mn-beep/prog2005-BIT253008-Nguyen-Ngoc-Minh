danh_sach_sach = [
    ("Book 1", 30000),
    ("Book 2", 50000),
    ("Book 3", 100000)
]
with open("books.txt", "w", encoding="utf-8") as file:
    for name, price in danh_sach_sach:
        file.write(f"{name};{price}\n")

print("Đã lưu thông tin sách vào file 'books.txt' thành công!")