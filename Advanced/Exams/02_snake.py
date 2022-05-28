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


size = int(input())

territory = [list(input()) for _ in range(size)]
snake_row = 0
snake_col = 0
burrows = []

for row in range(size):
    for col in range(size):
        if territory[row][col] == "S":
            snake_row, snake_col = row, col
        elif territory[row][col] == "B":
            burrows.append((row, col))

game_over = False
food_eaten = 0

while True:
    direction = input()
    next_row, next_col = next_position(snake_row, snake_col, direction)

    territory[snake_row][snake_col] = "."
    snake_row, snake_col = next_row, next_col

    if not valid_coordinates(snake_row, snake_col, size):
        game_over = True
        break

    if territory[next_row][next_col] == "*":
        food_eaten += 1

    elif territory[snake_row][snake_col] == "B":
        burrows.remove((snake_row, snake_col))
        territory[snake_row][snake_col] = "."
        exit_row, exit_col = burrows[0][0], burrows[0][1]
        snake_row, snake_col = exit_row, exit_col

    territory[snake_row][snake_col] = "S"

    if food_eaten == 10:
        break


if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_eaten}")

for row in territory:
    print(*row, sep="")
