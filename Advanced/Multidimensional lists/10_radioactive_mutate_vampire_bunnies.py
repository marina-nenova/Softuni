from collections import deque


def valid_coordinates(row_index, col_index, matrix_rows, matrix_cols):
    return 0 <= row_index < matrix_rows and 0 <= col_index < matrix_cols


def player_moves(direction, player_coordinates):
    player_row = player_coordinates[0]
    player_col = player_coordinates[1]

    matrix[player_row][player_col] = "."
    if direction == "U":
        player_row -= 1
    elif direction == "D":
        player_row += 1
    elif direction == "R":
        player_col += 1
    elif direction == "L":
        player_col -= 1

    return (player_row, player_col)


def bunnies_move(matrix_rows, matrix_cols):
    possible_moves = set()
    for row in range(matrix_rows):
        for col in range(matrix_cols):
            if matrix[row][col] == "B" and (row, col) not in bunnies_visited:
                bunnies_visited.add((row, col))
                if valid_coordinates(row - 1, col, matrix_rows, matrix_cols) and matrix[row - 1][col] != "B":
                    possible_moves.add((row - 1, col))
                if valid_coordinates(row, col + 1, matrix_rows, matrix_cols) and matrix[row][col + 1] != "B":
                    possible_moves.add((row, col + 1))
                if valid_coordinates(row + 1, col, matrix_rows, matrix_cols) and matrix[row + 1][col] != "B":
                    possible_moves.add((row + 1, col))
                if valid_coordinates(row, col - 1, matrix_rows, matrix_cols) and matrix[row][col - 1] != "B":
                    possible_moves.add((row, col - 1))

    return possible_moves


rows, cols = [int(el) for el in input().split()]
matrix = [list(input()) for _ in range(rows)]

player_coordinates = ()

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "P":
            player_coordinates = (row, col)


commands = deque(input())

player_won = False
bunnies_won = False

while not player_won and not bunnies_won:

    player_current_position = player_moves(commands.popleft(), player_coordinates)
    player_row, player_col = player_current_position[0], player_current_position[1]

    if not valid_coordinates(player_row, player_col, rows, cols):
        player_won = True
    elif matrix[player_row][player_col] == "B":
        bunnies_won = True
        player_coordinates = (player_row, player_col)
    else:
        matrix[player_row][player_col] = "P"
        player_coordinates = (player_row, player_col)

    bunnies_visited = set()
    bunnies_positions = bunnies_move(rows, cols)

    for position in bunnies_positions:
        r, c = position[0], position[1]
        if position == player_coordinates and not player_won:
            bunnies_won = True
        matrix[r][c] = "B"

for row in matrix:
    print(*row, sep="")

if player_won:
    print(f"won: {player_coordinates[0]} {player_coordinates[1]}")
if bunnies_won:
    print(f"dead: {player_coordinates[0]} {player_coordinates[1]}")