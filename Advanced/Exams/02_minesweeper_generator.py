def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def sum_bombs(row_index, col_index, size):
    bombs_count = 0
    if valid_coordinates(row - 1, col - 1, size) and field[row - 1][col - 1] == "*": # up left diagonal
        bombs_count += 1
    if valid_coordinates(row - 1, col, size) and field[row - 1][col] == "*": # up
        bombs_count += 1
    if valid_coordinates(row - 1, col + 1, size) and field[row - 1][col + 1] == "*": #up right diagonal
        bombs_count += 1
    if valid_coordinates(row, col - 1, size) and field[row][col - 1] == "*": # left
        bombs_count += 1
    if valid_coordinates(row, col + 1, size) and field[row][col + 1] == "*": # right
        bombs_count += 1
    if valid_coordinates(row + 1, col - 1, size) and field[row + 1][col - 1] == "*": #down left diagonal
        bombs_count += 1
    if valid_coordinates(row + 1, col, size) and field[row + 1][col] == "*": #down
        bombs_count += 1
    if valid_coordinates(row + 1, col + 1, size) and field[row + 1][col + 1] == "*": #down right diagonal
        bombs_count += 1
    return bombs_count


size = int(input())
number_of_bombs = int(input())
bombs = []
for _ in range(number_of_bombs):
    mine = input()
    bomb_position = [int(el) for el in mine[1: -1].split(", ")]
    bombs.append(bomb_position)

field = []

for row in range(size):
    current_line = []
    for col in range(size):
        if [row, col] in bombs:
            current_line.append("*")
        else:
            current_line.append("0")
    field.append(current_line)


for row in range(size):
    for col in range(size):
        if field[row][col] == "*":
            continue
        else:
            field[row][col] = sum_bombs(row, col, size)

for row in field:
    print(*row, sep=" ")
