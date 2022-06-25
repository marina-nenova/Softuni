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


size = 6

field = [input().split() for _ in range(size)]

rover_row = 0
rover_col = 0

for row in range(size):
    for col in range(size):
        if field[row][col] == "E":
            rover_row, rover_col = row, col

directions = input().split(", ")
deposits = {"W": "Water", "M": "Metal", "C": "Concrete"}
deposits_found = {}

for direction in directions:

    next_row, next_col = next_position(rover_row, rover_col, direction)
    field[rover_row][rover_col] = "-"
    rover_row, rover_col = next_row, next_col

    if field[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

    if field[rover_row][rover_col] in "W M C":
        letter = field[rover_row][rover_col]
        deposit_type = deposits[letter]
        print(f"{deposit_type} deposit found at ({rover_row}, {rover_col})")
        if deposit_type not in deposits_found:
            deposits_found[deposit_type] = 0
        deposits_found[deposit_type] += 1

    field[rover_row][rover_col] = "E"

if len(deposits_found) == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
