def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def next_position(row_index, col_index, current_direction, steps):
    steps_made = []

    for step in range(steps):

        if current_direction == "up":
            row_index = rows - 1 if row_index == 0 else row_index - 1
        elif current_direction == "down":
            row_index = 0 if row_index == rows - 1 else row_index + 1
        elif current_direction == "left":
            col_index = cols - 1 if col_index == 0 else col_index - 1
        elif current_direction == "right":
            col_index = 0 if col_index == cols - 1 else col_index + 1

        steps_made.append((row_index, col_index))

    return steps_made


rows, cols = [int(el) for el in input().split(", ")]

field = []

player_row = 0
player_col = 0
items = 0

for row in range(rows):
    line = input().split()
    for col in range(cols):
        if line[col] == "Y":
            player_row, player_col = row, col
        elif line[col] in "G D C":
            items += 1
    field.append(line)

items_collected = {"Christmas decorations": 0, "Gifts": 0, "Cookies": 0}
command = input()

while not command == "End":
    data = command.split("-")
    direction = data[0]
    steps = int(data[1])
    field[player_row][player_col] = "x"
    next_positions = next_position(player_row, player_col, direction, steps)

    for row, col in next_positions:
        field[player_row][player_col] = "x"
        player_row, player_col = row, col

        if field[player_row][player_col] == "D":
            items_collected["Christmas decorations"] += 1
            items -= 1
        elif field[player_row][player_col] == "G":
            items_collected["Gifts"] += 1
            items -= 1
        elif field[player_row][player_col] == "C":
            items_collected["Cookies"] += 1
            items -= 1

        field[player_row][player_col] = "Y"

        if not items:
            break

    if not items:
        print("Merry Christmas!")
        break

    command = input()

print("You've collected:")

for item, count in items_collected.items():
    print(f"- {count} {item}")

for row in field:
    print(*row, end="\n")