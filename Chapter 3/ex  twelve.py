# Giả sử ta có 2 ma trận 2x3
matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[7, 8, 9], [10, 11, 12]]

rows = len(matrix_a)
cols = len(matrix_a[0])
matrix_c = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]

print("Ma trận tổng:")
for row in matrix_c:
    print(row)