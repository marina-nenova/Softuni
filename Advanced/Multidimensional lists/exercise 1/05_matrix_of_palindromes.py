rows, cols = [int(el) for el in input().split()]
matrix = []


for row in range(rows):
    first_symbol = ord("a") + row
    current_row = []
    for col in range(cols):
        current_row.append(chr(first_symbol) + chr(first_symbol + col) + chr(first_symbol))
    matrix.append(current_row)

for row in matrix:
    print(*row)