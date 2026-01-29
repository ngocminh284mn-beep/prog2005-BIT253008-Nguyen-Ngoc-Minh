# Định nghĩa hàm với giá trị mặc định name="Student"
def greet(name="Student"):
    print("Hello, " + name + "!")

# Trường hợp 1: Gọi hàm KHÔNG có đối số
# (Máy tính sẽ tự lấy "Student")
greet()

# Trường hợp 2: Gọi hàm CÓ đối số
# (Máy tính sẽ lấy tên bạn nhập vào)
greet("Minh")