import math # Thư viện toán học để tính căn

so = float(input("Nhập một số: "))

if so < 0:
    print("Lỗi: Không thể tính căn bậc hai của số âm.")
else:
    print("Căn bậc hai là:", math.sqrt(so))