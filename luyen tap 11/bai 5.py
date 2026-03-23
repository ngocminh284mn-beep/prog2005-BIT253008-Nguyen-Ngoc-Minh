my_dict = {
    'tên': 'Minh',
    'tuổi': 24,
    'nghành học': 'Cntt'}
key_can_tim = input("Nhập 'key' bạn muốn kiểm tra: ")
if key_can_tim in my_dict:
    print(f"Key '{key_can_tim}' CÓ tồn tại trong dictionary (Giá trị: {my_dict[key_can_tim]}).")
else:
    print(f"Key '{key_can_tim}' KHÔNG tồn tại trong dictionary.")