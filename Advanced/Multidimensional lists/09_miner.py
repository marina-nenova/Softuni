def move(position, direction):
    current_position = position
    if direction == "up" and current_position[0] - 1 >= 0:
        current_position[0] = current_position[0] - 1
    elif direction == "down" and current_position[0] + 1 < rows:
        current_position[0] = current_position[0] + 1
    elif direction == "right" and current_position[1] + 1 < rows:
        current_position[1] = current_position[1] + 1
    elif direction == "left" and current_position[1] - 1 >= 0:
        current_position[1] = current_position[1] - 1
    return current_position


rows = int(input())
commands = input().split()

field_matrix = []

for _ in range(rows):
    line = input().split()
    field_matrix.append(line)

start = []
coal_count = 0

for row in range(rows):
    for col in range(rows):
        if field_matrix[row][col] == "s":
            start = [row, col]
        elif field_matrix[row][col] == "c":
            coal_count += 1

game_over = False
all_collected = False
coal_collected = 0

for direction in commands:
    current_position = move(start, direction)
    row_index = current_position[0]
    col_index = current_position[1]
    if field_matrix[row_index][col_index] == "e":
        game_over = True
        print(f"Game over! ({row_index}, {col_index})")
        break
    elif field_matrix[row_index][col_index] == "c":
        coal_collected += 1
        field_matrix[row_index][col_index] = "*"
        if coal_collected == coal_count:
            all_collected = True
            print(f"You collected all coal! ({row_index}, {col_index})")
    start = current_position

if not all_collected and not game_over:
    remaining_coal = coal_count - coal_collected
    print(f"{remaining_coal} pieces of coal left. ({start[0]}, {start[1]})")