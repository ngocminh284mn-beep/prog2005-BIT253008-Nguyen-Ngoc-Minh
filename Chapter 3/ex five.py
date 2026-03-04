user_input = input("Nhập danh sách số thực (cách nhau bằng khoảng trắng): ")
float_list = [float(x) for x in user_input.split()]

for i in range(1, len(float_list)):
    key = float_list[i]
    j = i - 1
    # Đổi dấu > để sắp xếp giảm dần
    while j >= 0 and key > float_list[j]:
        float_list[j + 1] = float_list[j]
        j -= 1
    float_list[j + 1] = key

print("Danh sách giảm dần (Insertion Sort):", float_list)