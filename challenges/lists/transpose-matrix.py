matrix = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
transposed_matrix = []

for x in range(4):
    s = []
    for y in range(3):
        s.append(matrix[y][x])
    transposed_matrix.append(s)

print(transposed_matrix)