rows = int(input())
matrix = []

for _ in range(rows):
    line = [int(el) for el in input().split(", ")]
    matrix.append(line)

sorted_matrix = [[el for el in row if el %2 == 0]for row in matrix]

print(sorted_matrix)