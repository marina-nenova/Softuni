rows = int(input())
matrix = []

for _ in range(rows):
    line = [int(el) for el in input().split()]
    matrix.append(line)

diagonal_sum = 0
for row in range(rows):
    diagonal_sum += matrix[row][row]

print(diagonal_sum)