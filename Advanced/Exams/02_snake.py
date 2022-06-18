def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'down': lambda r, c: (r + 1, c),
    'up': lambda r, c: (r - 1, c)
}


size = int(input())

field = [list(input()) for _ in range(size)]

snake_row = 0
snake_col = 0
burrows = []
for row in range(size):
    for col in range(size):
        if field[row][col] == "S":
            snake_row, snake_col = row, col
        elif field[row][col] == "B":
            burrows.append((row, col))

food_quantity = 0
success = False

while True:
    direction = input()
    next_row, next_col = directions[direction](snake_row, snake_col)

    field[snake_row][snake_col] = "."
    snake_row, snake_col = next_row, next_col

    if not valid_coordinates(snake_row, snake_col, size):
        break

    if (snake_row, snake_col) in burrows:
        burrows.remove((snake_row, snake_col))
        field[snake_row][snake_col] = "."
        snake_row, snake_col = burrows.pop()

    elif field[snake_row][snake_col] == "*":
        food_quantity += 1
        if food_quantity == 10:
            success = True
            field[snake_row][snake_col] = "S"
            break

    field[snake_row][snake_col] = "S"

if success:
    print("You won! You fed the snake.")
else:
    print("Game over!")

print(f"Food eaten: {food_quantity}")

for row in field:
    print(*row, sep="")

