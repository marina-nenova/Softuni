def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def get_next_position(row, col, direction):
    if direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col
    elif direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1


presents = int(input())
size = int(input())

neighbourhood = [input().split() for _ in range(size)]
nice_kids = 0
santa_row = 0
santa_col = 0


for row in range(size):
    for col in range(size):
        if neighbourhood[row][col] == "S":
            santa_row, santa_col = row, col
        elif neighbourhood[row][col] == "V":
            nice_kids += 1

command = input()
nice_kids_happy = 0

while not command == "Christmas morning":
    next_row, next_col = get_next_position(santa_row, santa_col, command)

    if not valid_coordinates(next_row, next_col, size):
        continue

    neighbourhood[santa_row][santa_col] = "-"
    santa_row, santa_col = next_row, next_col

    if neighbourhood[santa_row][santa_col] == "V":
        presents -= 1
        nice_kids_happy += 1

    elif neighbourhood[santa_row][santa_col] == "C":

        for direction in ["left", "right", "up", "down"]:
            current_row, current_col = get_next_position(santa_row, santa_col, direction)

            if neighbourhood[current_row][current_col] == "V" or neighbourhood[current_row][current_col] == "X":
                presents -= 1

                if neighbourhood[current_row][current_col] == "V":
                    nice_kids_happy += 1
                neighbourhood[current_row][current_col] = "-"

                if presents == 0:
                    break

    neighbourhood[santa_row][santa_col] = "S"

    if presents == 0:
        break

    command = input()

if presents == 0 and nice_kids_happy != nice_kids:
    print("Santa ran out of presents!")

for row in neighbourhood:
    print(*row, sep=" ")

if nice_kids_happy == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    difference = nice_kids - nice_kids_happy
    print(f"No presents for {difference} nice kid/s.")
