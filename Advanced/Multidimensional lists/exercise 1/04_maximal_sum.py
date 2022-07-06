import sys

rows, cols = [int(el) for el in input().split()]

matrix = []

for _ in range(rows):
    line = [int(el) for el in input().split()]
    matrix.append(line)
max_sum = -sys.maxsize
max_sub_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        sub_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
                      matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2],
                      matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sub_matrix = sub_matrix

print(f"Sum = {max_sum}")
print(max_sub_matrix[0], max_sub_matrix[1], max_sub_matrix[2])
print(max_sub_matrix[3], max_sub_matrix[4], max_sub_matrix[5])
print(max_sub_matrix[6], max_sub_matrix[7], max_sub_matrix[8])
