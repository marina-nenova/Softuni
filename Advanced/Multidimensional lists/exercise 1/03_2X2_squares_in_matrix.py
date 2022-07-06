
rows, cols = [int(el) for el in input().split()]
matrix = []

for _ in range(rows):
    line = input().split()
    matrix.append(line)

identical_symbols_count = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        sub_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]
        if len(set(sub_matrix)) == 1:
            identical_symbols_count += 1

print(identical_symbols_count)
