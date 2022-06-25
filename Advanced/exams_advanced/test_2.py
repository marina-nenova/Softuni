def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'down': lambda r, c: (r + 1, c),
    'up': lambda r, c: (r - 1, c)
}

size = int(input())

wall = []

vanko_row = 0
vanko_col = 0

for row in range(size):
    line = list(input())
    for col in range(size):
        if line[col] == "V":
            vanko_row, vanko_col = row, col
    wall.append(line)

holes_made = 1
rods_hit = 0
electrocuted = False

while True:
    direction = input()
    if direction == "End":
        break

    next_row, next_col = directions[direction](vanko_row, vanko_col)

    if valid_coordinates(next_row, next_col, size):

        if wall[next_row][next_col] == "R":
            rods_hit += 1
            print("Vanko hit a rod!")
            continue

        wall[vanko_row][vanko_col] = "*"
        vanko_row, vanko_col = next_row, next_col

        if wall[vanko_row][vanko_col] == "C":
            wall[vanko_row][vanko_col] = "E"
            holes_made += 1
            electrocuted = True
            break
        elif wall[vanko_row][vanko_col] == "*":
            print(f"The wall is already destroyed at position [{vanko_row}, {vanko_row}]!")
        else:
            holes_made += 1

        wall[vanko_row][vanko_col] = "V"


if not electrocuted:
    print(f"Vanko managed to make {holes_made} hole(s) and he hit only {rods_hit} rod(s).")
else:
    print(f"Vanko got electrocuted, but he managed to make {holes_made} hole(s).")

for row in wall:
    print(*row, sep="")
