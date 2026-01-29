try:
    a = int(input("Nhập số bị chia: "))
    b = int(input("Nhập số chia: "))

    ket_qua = a / b
    print("Kết quả phép chia:", ket_qua)

except ZeroDivisionError:
    print("Lỗi: Không thể chia một số cho 0.")
except ValueError:
    print("Lỗi: Vui lòng chỉ nhập số nguyên.")