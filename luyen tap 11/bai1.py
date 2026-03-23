def get_sorted_strings():
    strings = [input(f"Nhập chuỗi {i + 1}: ") for i in range(5)]
    for i in range(1, len(strings)):
        key = strings[i]
        j = i - 1
        while j >= 0 and len(strings[j]) < len(key):
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = key
        print(f"Bước {i}: {strings}")
    return strings
if __name__ == "__main__":
    result = get_sorted_strings()
    print("Kết quả bài 1:", result)