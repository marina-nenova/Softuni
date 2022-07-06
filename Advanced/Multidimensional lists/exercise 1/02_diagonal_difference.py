rows = int(input())

matrix = []

for _ in range(rows):
    line = [int(el) for el in input().split()]
    matrix.append(line)

primary_diagonal = []
secondary_diagonal = []

for row in range(rows):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][rows - 1 - row])

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)

difference = abs(primary_sum - secondary_sum)

print(difference)