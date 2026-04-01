import matplotlib.pyplot as plt
san_pham = ['A', 'B', 'C', 'D', 'E']
phan_tram = [30, 25, 15, 20, 10]
plt.pie(phan_tram, labels=san_pham, autopct='%1.1f%%')
plt.title('Ti le doanh so cac san pham')
plt.show()