def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def get_next_position(row, col, direction, steps):
    if direction == "up":
        return row - steps, col
    elif direction == "down":
        return row + steps, col
    elif direction == "left":
        return row, col - steps
    elif direction == "right":
        return row, col + steps


size = 5
matrix = [input().split() for _ in range(size)]
player_row = 0
player_col = 0
targets = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "A":
            player_row, player_col = row, col
        elif matrix[row][col] == "x":
            targets += 1

n = int(input())
targets_shot = []

for _ in range(n):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == "move":
        steps = int(command[2])
        next_row, next_col = get_next_position(player_row, player_col, direction, steps)

        if not valid_coordinates(next_row, next_col, size) or matrix[next_row][next_col] != ".":
            continue
        matrix[player_row][player_col] = "."
        player_row, player_col = next_row, next_col
        matrix[player_row][player_col] = "A"

    elif action == "shoot":
        shot_row, shot_col = player_row, player_col

        while True:
            shot_row, shot_col = get_next_position(shot_row, shot_col, direction, 1)
            if not valid_coordinates(shot_row, shot_col, size):
                break
            if matrix[shot_row][shot_col] == "x":
                matrix[shot_row][shot_col] = "."
                targets_shot.append([shot_row, shot_col])
                break

        if len(targets_shot) == targets:
            break

targets_hit_count = len(targets_shot)

if targets == targets_hit_count:
    print(f"Training completed! All {targets} targets hit.")
else:
    difference = targets - targets_hit_count
    print(f"Training not completed! {difference} targets left.")

for target in targets_shot:
    print(target)
