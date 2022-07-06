rows, cols = [int(el) for el in input().split(", ")]
matrix = []

for _ in range(rows):
    line = [int(el) for el in input().split()]
    matrix.append(line)

for col in range(cols):
    col_sum = 0
    for row in range(rows):
        col_sum += matrix[row][col]
    print(col_sum)

