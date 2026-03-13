def kiem_tra_key(tu_dien, key_can_tim):
    if key_can_tim in tu_dien:
        print(f"Key '{key_can_tim}' có tồn tại.")
    else:
        print(f"Key '{key_can_tim}' không tồn tại.")
thong_tin = {"ten": "Sinh Viên", "tuoi": 19}

print("\n--- Bài 3 ---")
kiem_tra_key(thong_tin, "ten")   # Sẽ in ra có tồn tại
kiem_tra_key(thong_tin, "diem")  # Sẽ in ra không tồn tại