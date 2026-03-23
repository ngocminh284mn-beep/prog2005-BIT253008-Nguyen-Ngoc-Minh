def nhap_ma_tran(ten_ma_tran, rows, cols):
    matrix = []
    print(f"\n--- Nhập dữ liệu cho ma trận {ten_ma_tran} ---")
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                val = input(f"Nhập phần tử {ten_ma_tran}[{i}][{j}]: ")
                if val.strip() == "":
                    print(" Lỗi: Bạn không được để trống giá trị. Vui lòng nhập lại!")
                    continue

                try:
                    num = float(val)
                    row.append(num)
                    break
                except ValueError:
                    print(" Lỗi: Giá trị nhập vào phải là một số. Vui lòng nhập lại!")
        matrix.append(row)
    return matrix
def cong_ma_tran():
    print("CHƯƠNG TRÌNH CỘNG HAI MA TRẬN CÙNG KÍCH THƯỚC")
    while True:
        try:
            r_input = input("\nNhập số hàng của ma trận: ")
            if r_input.strip() == "":
                print(" Lỗi: Không được để trống. Vui lòng nhập lại!")
                continue
            rows = int(r_input)

            c_input = input("Nhập số cột của ma trận: ")
            if c_input.strip() == "":
                print(" Lỗi: Không được để trống. Vui lòng nhập lại!")
                continue
            cols = int(c_input)

            if rows <= 0 or cols <= 0:
                print(" Lỗi: Số hàng và cột phải lớn hơn 0.")
                continue
            break
        except ValueError:
            print(" Lỗi: Kích thước ma trận phải là số nguyên hợp lệ.")
    A = nhap_ma_tran("A", rows, cols)
    B = nhap_ma_tran("B", rows, cols)
    C = []
    for i in range(rows):
        row_c = []
        for j in range(cols):
            # C[i][j] = A[i][j] + B[i][j]
            row_c.append(A[i][j] + B[i][j])
        C.append(row_c)
    print("\n Ma trận kết quả C (A + B) là:")
    for row in C:
        print(row)
if __name__ == "__main__":
    cong_ma_tran()