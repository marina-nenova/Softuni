def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def next_position(row_index, col_index, current_direction):
    if current_direction == "up":
        row_index -= 1
    elif current_direction == "down":
        row_index += 1
    elif current_direction == "left":
        col_index -= 1
    elif current_direction == "right":
        col_index += 1

    return row_index, col_index


text = input()
size = int(input())

field = [list(input()) for _ in range(size)]

player_row = 0
player_col = 0

for row in range(size):
    for col in range(size):
        if field[row][col] == "P":
            player_row, player_col = row, col

directions_count = int(input())


for _ in range(directions_count):

    direction = input()
    next_row, next_col = next_position(player_row, player_col, direction)

    if not valid_coordinates(next_row, next_col, size):
        if text:
            text = text[:-1]
        continue

    field[player_row][player_col] = "-"
    player_row, player_col = next_row, next_col
    current_symbol = field[player_row][player_col]

    if current_symbol.isalpha():
        text += current_symbol

    field[player_row][player_col] = "P"


print(text)

for row in field:
    print(*row, sep="")