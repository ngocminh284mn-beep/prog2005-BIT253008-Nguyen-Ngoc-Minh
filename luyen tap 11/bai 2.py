from bai1 import get_sorted_strings

strings = get_sorted_strings()
target = input("\nNhập chuỗi cần tìm trong danh sách trên: ")
low, high = 0, len(strings) - 1
pos = -1

while low <= high:
    mid = (low + high) // 2
    if strings[mid] == target:
        pos = mid
        break
    elif len(strings[mid]) < len(target):
        high = mid - 1
    else:
        low = mid + 1

print(f"{pos}" if pos != -1 else "Không tìm thấy")