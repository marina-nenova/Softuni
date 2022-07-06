def valid_coordinates(row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[row])


def cells_places(row, col):
    cells = []
    if valid_coordinates(row - 1, col - 1) and matrix[row - 1][col - 1] > 0:  # check up left diagonal and if first row or first column
        cells.append((row - 1, col - 1))
    if valid_coordinates(row - 1, col) and matrix[row - 1][col] > 0:  # check up and if first row
        cells.append((row - 1, col))
    if valid_coordinates(row - 1, col + 1) and matrix[row - 1][col + 1] > 0:  # check up right diagonal and if first row or last column
        cells.append((row - 1, col + 1))
    if valid_coordinates(row, col + 1) and matrix[row][col + 1] > 0:  # check right
        cells.append((row, col + 1))
    if valid_coordinates(row + 1, col + 1) and matrix[row + 1][col + 1] > 0:  # check down right diagonal and last row or last column
        cells.append((row + 1, col + 1))
    if valid_coordinates(row + 1, col) and matrix[row + 1][col] > 0:  # check down
        cells.append((row + 1, col))
    if valid_coordinates(row + 1, col - 1) and matrix[row + 1][col - 1] > 0:  # check down left diagonal and if first row or first column
        cells.append((row + 1, col - 1))
    if valid_coordinates(row, col - 1) and matrix[row][col - 1] > 0:  # check left and if first column
        cells.append((row, col - 1))
    return cells


rows = int(input())
matrix = []

for _ in range(rows):
    line = [int(el) for el in input().split()]
    matrix.append(line)

data = input().split()
coordinates = [[int(num) for num in el.split(",")] for el in data]

for row, col in coordinates:
    bomb_strength = matrix[row][col]
    if bomb_strength > 0:
        cells_to_destroy = cells_places(row, col)
        for r, c in cells_to_destroy:
            matrix[r][c] -= bomb_strength
        matrix[row][col] = 0

active_cells_sum = 0
active_cells_count = 0

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] > 0:
            active_cells_count += 1
            active_cells_sum += matrix[row][col]

print(f"Alive cells: {active_cells_count}")
print(f"Sum: {active_cells_sum}")

for row in matrix:
    print(*row, sep=" ")