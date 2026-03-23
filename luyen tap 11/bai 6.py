thong_tin = {}
n = int(input("Bạn muốn nhập thông tin cho bao nhiêu người? "))
for i in range(n):
    ten = input(f"Nhập tên người thứ {i+1}: ")
    tuoi = int(input(f"Nhập tuổi của {ten}: "))
    thong_tin[ten] = tuoi

print("\nThông tin Dictionary đã lưu:", thong_tin)
if thong_tin:
    tuoi_trung_binh = sum(thong_tin.values()) / len(thong_tin)
    print(f"Tuổi trung bình của {len(thong_tin)} người là: {tuoi_trung_binh}")
else:
    print("Bạn chưa nhập dữ liệu nào.")