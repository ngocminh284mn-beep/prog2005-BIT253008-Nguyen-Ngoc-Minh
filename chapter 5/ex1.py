import matplotlib.pyplot as plt
xep_loai = ['Xuất sắc', 'Giỏi', 'Trung bình', 'Yếu', 'Kém']
so_luong = [6, 10, 12, 4, 1]
plt.bar(xep_loai, so_luong)
plt.title('Ket qua hoc tap cua lop') # Tiêu đề
plt.xlabel('Phan loai')             # Nhãn trục ngang
plt.ylabel('So luong hoc sinh')     # Nhãn trục đứng
plt.show()