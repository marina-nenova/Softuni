def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def place_numbers(bomb_row, bomb_col):
    possible_positions = [
        (bomb_row - 1, bomb_col - 1),
        (bomb_row - 1, bomb_col),
        (bomb_row - 1, bomb_col + 1),
        (bomb_row + 1, bomb_col + 1),
        (bomb_row + 1, bomb_col),
        (bomb_row + 1, bomb_col - 1),
        (bomb_row, bomb_col - 1),
        (bomb_row, bomb_col + 1)
    ]

    for row, col in possible_positions:
        if valid_coordinates(row, col, size) and field[row][col] != "*":
            field[row][col] += 1


size = int(input())
number_of_bombs = int(input())
bombs = []

for _ in range(number_of_bombs):
    bomb_position = eval(input())
    bombs.append(bomb_position)

field = []

for row in range(size):
    line = []
    for col in range(size):
        if (row, col) in bombs:
            line.append("*")
        else:
            line.append(0)
    field.append(line)

for bomb in bombs:
    bomb_row, bomb_col = bomb
    place_numbers(bomb_row, bomb_col)

for row in field:
    print(*row, sep=" ")
