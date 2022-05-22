import sys

rows, cols = [int(el) for el in input().split(", ")]
matrix = []

for _ in range(rows):
    line = [int(el) for el in input().split(", ")]
    matrix.append(line)

max_sum = -sys.maxsize
max_sub_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        sub_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]
        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sub_matrix = sub_matrix

print(max_sub_matrix[0], max_sub_matrix[1])
print(max_sub_matrix[2], max_sub_matrix[3])
print(max_sum)
