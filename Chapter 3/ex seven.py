arr_input = input("Nhập danh sách số (cách nhau bằng khoảng trắng): ")
arr = [int(x) for x in arr_input.split()]
target = int(input("Nhập số cần tìm: "))

index = -1
for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break

if index != -1:
    print(f"Số {target} nằm ở chỉ số {index}.")
else:
    print(f"Không tìm thấy số {target}.")