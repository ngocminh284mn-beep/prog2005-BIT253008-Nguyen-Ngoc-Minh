weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

bmi = weight / (height * height)

# Làm tròn 2 chữ số thập phân bằng hàm round()
print("Chỉ số BMI của bạn là:", round(bmi, 2))