import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = x**2
y2 = np.sqrt(x)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, y1, color='blue')
ax1.set_title("Đồ thị y = x^2")
ax1.set_xlabel("Trục X")
ax1.set_ylabel("Trục Y")
ax2.plot(x, y2, color='red')
ax2.set_title("Đồ thị y = sqrt(x)")
ax2.set_xlabel("Trục X")
ax2.set_ylabel("Trục Y")
plt.tight_layout()
plt.show()