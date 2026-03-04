text = input("Nhập một chuỗi: ")

if text == text[::-1]:
    print("Đây là chuỗi Palindrome (đối xứng).")
else:
    print("Đây không phải chuỗi Palindrome.")