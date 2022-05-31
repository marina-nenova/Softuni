def valid_coordinates(row_index, col_index, rows, cols):
    return 0 <= row_index < rows and 0 <= col_index < cols


def next_position(row_index, col_index, current_direction, steps):
    steps_made = []
    for step in range(steps):
        if current_direction == "up":
            row_index -= 1
            if row_index < 0:
                row_index = rows - 1
        elif current_direction == "down":
            row_index += 1
            if row_index >= rows:
                row_index = 0
        elif current_direction == "left":
            col_index -= 1
            if col_index < 0:
                col_index = cols - 1
        elif current_direction == "right":
            col_index += 1
            if col_index >= cols:
                col_index = 0
        steps_made.append((row_index, col_index))
    return steps_made


rows, cols = [int(el) for el in input().split(", ")]

workshop = [input().split() for _ in range(rows)]

player_row = 0
player_col = 0
items = []

for row in range(rows):
    for col in range(cols):
        if workshop[row][col] == "Y":
            player_row, player_col = row, col
        elif workshop[row][col] in "D G C":
            items.append((row, col))

collected_items = {"Christmas decorations": 0, "Gifts": 0, "Cookies": 0}
command = input()

while not command == "End":
    data = command.split("-")
    direction = data[0]
    steps = int(data[1])
    next_steps = next_position(player_row, player_col, direction, steps)

    for next_row, next_col in next_steps:
        if not items:
            break
        workshop[player_row][player_col] = "x"
        player_row, player_col = next_row, next_col
        if workshop[player_row][player_col] == "D":
            collected_items["Christmas decorations"] += 1
            items.remove((player_row, player_col))
        elif workshop[player_row][player_col] == "G":
            collected_items["Gifts"] += 1
            items.remove((player_row, player_col))
        elif workshop[player_row][player_col] == "C":
            collected_items["Cookies"] += 1
            items.remove((player_row, player_col))
        workshop[player_row][player_col] = "Y"

    if not items:
        break

    command = input()

if not items:
    print("Merry Christmas!")

print("You've collected:")

for item, count in collected_items.items():
    print(f"- {count} {item}")

for row in workshop:
    print(*row, sep=" ")