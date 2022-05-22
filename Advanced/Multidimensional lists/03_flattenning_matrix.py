rows = int(input())
matrix = []

for _ in range(rows):
    line = [int(el) for el in input().split(", ")]
    matrix.append(line)

flattened_matrix = [el for row in matrix for el in row]

print(flattened_matrix)


# rows = int(input())
# matrix = []
#
# for _ in range(rows):
#     line = [int(el) for el in input().split(", ")]
#     matrix.extend(line)
#
# print(matrix)