def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
mang_vi_du = [64, 25, 12, 22, 11]
print("Mảng trước khi sắp xếp:", mang_vi_du)
mang_da_sap_xep = selection_sort(mang_vi_du)
print("Mảng sau khi sắp xếp bằng Selection Sort:", mang_da_sap_xep)