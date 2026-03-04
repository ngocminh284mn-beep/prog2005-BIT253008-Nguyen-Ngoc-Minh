nums = [64, 34, 25, 12, 22, 11, 90]
swaps = 0
n = len(nums)

for i in range(n):
    for j in range(0, n-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            swaps += 1

print("Danh sách đã sắp xếp (Bubble Sort):", nums)
print("Tổng số lần hoán đổi:", swaps)