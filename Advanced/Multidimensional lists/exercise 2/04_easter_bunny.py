import sys


def valid_coordinates(row_index, col_index):
    return 0 <= row_index < rows and 0 <= col_index < rows


def collect_eggs(row_index, col_index, current_direction):
    current_eggs_count = 0
    bunny_path = []

    while True:
        if current_direction == "up":
            row_index -= 1
        elif current_direction == "down":
            row_index += 1
        elif current_direction == "left":
            col_index -= 1
        elif current_direction == "right":
            col_index += 1

        if not valid_coordinates(row_index, col_index) or matrix[row_index][col_index] == "X":
            break
        else:
            bunny_path.append([row_index, col_index])
            current_eggs_count += int(matrix[row_index][col_index])

    return current_eggs_count, bunny_path


rows = int(input())

matrix = [input().split() for _ in range(rows)]

bunny_row = 0
bunny_col = 0

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "B":
            bunny_row, bunny_col = row, col

max_eggs_count = -sys.maxsize
best_path = []
best_direction = ""
possible_directions = ["up", "down", "left", "right"]

for direction in possible_directions:

    current_eggs, current_path = collect_eggs(bunny_row, bunny_col, direction)

    if current_eggs > max_eggs_count and current_path:
        max_eggs_count = current_eggs
        best_path = current_path
        best_direction = direction

print(best_direction)
print(*best_path, sep="\n")
print(max_eggs_count)
