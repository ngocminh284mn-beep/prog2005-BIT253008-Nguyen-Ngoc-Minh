colors = ["Red", "Blue", "Yellow", "Black", "White"]

try:
    colors.remove("Green")
except ValueError:
    print("Màu 'Green' không có trong danh sách.")

print("Danh sách hiện tại:", colors)