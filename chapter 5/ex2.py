import matplotlib.pyplot as plt
x = [i for i in range(-10, 11)]
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]
plt.plot(x, y1, label='y = x^2', color='blue')
plt.plot(x, y2, label='y = x^3', color='red')
plt.title('Do thi ham so')
plt.legend() # Hiển thị bảng chú thích (cái khung nhỏ góc biểu đồ)
plt.grid(True) # Thêm ô lưới cho dễ nhìn
plt.show()