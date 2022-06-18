def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def next_position(row_index, col_index, current_direction):
    if current_direction == "up":
        row_index -= 1
        if row_index < 0:
            row_index = size - 1
    elif current_direction == "down":
        row_index += 1
        if row_index >= size:
            row_index = 0
    elif current_direction == "left":
        col_index -= 1
        if col_index < 0:
            col_index = size - 1
    elif current_direction == "right":
        col_index += 1
        if col_index >= size:
            col_index = 0
    return row_index, col_index


size = int(input())

field = [input().split() for _ in range(size)]

player_row = 0
player_col = 0

for row in range(size):
    for col in range(size):
        if field[row][col] == "P":
            player_row, player_col = row, col

possible_commands = ["up", "down", "left", "right"]
player_path = [[player_row, player_col]]
total_coins = 0
failed = False

while True:
    direction = input()
    if direction not in possible_commands:
        continue

    next_row, next_col = next_position(player_row, player_col, direction)
    field[player_row][player_col] = "."
    player_row, player_col = next_row, next_col
    player_path.append([player_row, player_col])

    if field[player_row][player_col] == "X":
        failed = True
        break

    elif field[player_row][player_col].isdigit():
        coins = field[player_row][player_col]
        total_coins += int(field[player_row][player_col])

    field[player_row][player_col] = "P"

    if total_coins >= 100:
        break

if failed:
    print(f"Game over! You've collected {total_coins // 2} coins.")
else:
    print(f"You won! You've collected {total_coins} coins.")

print("Your path:")
for coordinates in player_path:
    print(coordinates)