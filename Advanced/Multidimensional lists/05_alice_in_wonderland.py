def valid_coordinates(row_index, col_index):
    return 0 <= row_index < rows and 0 <= col_index < rows


def move(row_index, col_index, current_direction):
    if current_direction == "up":
        row_index -= 1
    elif current_direction == "down":
        row_index += 1
    elif current_direction == "left":
        col_index -= 1
    elif current_direction == "right":
        col_index += 1
    return row_index, col_index


rows = int(input())

matrix = [input().split() for _ in range(rows)]

alice_position = ()

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "A":
            alice_position = (row, col)
            matrix[row][col] = "*"

total_bags_of_tea = 0
success = False

while True:
    direction = input()
    alice_row, alice_col = move(alice_position[0], alice_position[1], direction)
    alice_position = (alice_row, alice_col)
    if not valid_coordinates(alice_row, alice_col):
        break
    else:
        if matrix[alice_row][alice_col] == "R":
            matrix[alice_row][alice_col] = "*"
            break
        elif matrix[alice_row][alice_col].isdigit():
            tea_bags = int(matrix[alice_row][alice_col])
            total_bags_of_tea += tea_bags
            matrix[alice_row][alice_col] = "*"
            if total_bags_of_tea >= 10:
                success = True
                break
        matrix[alice_row][alice_col] = "*"


if success:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row)