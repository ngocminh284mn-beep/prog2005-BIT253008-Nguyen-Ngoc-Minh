import matplotlib.pyplot as plt

thanh_pho = [
    'Los Angeles', 'San Diego', 'San Jose', 'San Francisco',
    'Bakersfield', 'Fresno', 'Sacramento', 'Riverside',
    'Long Beach', 'Oakland'
]

dien_tich = [1302, 964, 466, 121, 396, 290, 259, 210, 208, 202]
thanh_pho.reverse()
dien_tich.reverse()
plt.barh(thanh_pho, dien_tich, color='green')
plt.title('Top 10 thanh pho lon nhat California')
plt.xlabel('Dien tich (km2)')
plt.ylabel('Ten thanh pho')
plt.show()