def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def attack(player_row, player_col, current_player):
    possible_moves = {
        "White": [(player_row - 1, player_col - 1), (player_row - 1, player_col + 1)],
        "Black": [(player_row + 1, player_col - 1), (player_row + 1, player_col + 1)]
    }
    for row, col in possible_moves[current_player]:
        if valid_coordinates(row, col, size) and field[row][col] != "-":
            return True
    return False


size = 8
field = [input().split() for _ in range(size)]

board = []

for row in range(size):
    current_row = []
    for col in range(size):
        current_square = f'{chr(ord("a") + col)}{size - row}'
        current_row.append(current_square)
    board.append(current_row)


players_coordinates = {"White": (), "Black": ()}

for row in range(size):
    for col in range(size):
        if field[row][col] == "w":
            players_coordinates["White"] = (row, col)
        elif field[row][col] == "b":
            players_coordinates["Black"] = (row, col)

current_player = "White"
next_player = "Black"

promoted = False
captured = False

while True:
    player_row, player_col = players_coordinates[current_player][0], players_coordinates[current_player][1]

    captured = attack(player_row, player_col, current_player)

    if captured:
        break

    field[player_row][player_col] = "-"

    if current_player == "White":
        player_row -= 1
        field[player_row][player_col] = "a"
        if player_row == 0:
            promoted = True

    elif current_player == "Black":
        player_row += 1
        field[player_row][player_col] = "b"
        if player_row == 7:
            promoted = True

    players_coordinates[current_player] = (player_row, player_col)

    if promoted:
        break

    current_player, next_player = next_player, current_player


if promoted:
    promotion_row, promotion_col = players_coordinates[current_player][0], players_coordinates[current_player][1]
    print(f"Game over! {current_player} pawn is promoted to a queen at {board[promotion_row][promotion_col]}.")

elif captured:
    capture_row, capture_col = players_coordinates[next_player][0], players_coordinates[next_player][1]
    print(f"Game over! {current_player} win, capture on {board[capture_row][capture_col]}.")
