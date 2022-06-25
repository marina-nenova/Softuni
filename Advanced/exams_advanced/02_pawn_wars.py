def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def possible_attacks(row, col, player):

    possible_moves = {
        "White": [(row - 1, col - 1), (row - 1, col + 1)],
        "Black": [(row + 1, col - 1), (row + 1, col + 1)]
    }

    for row, col in possible_moves[player]:
        if valid_coordinates(row, col, size) and field[row][col] != "-":
            return True

    return False


def create_board(size):
    board = []
    for row in range(size):
        current_row = []
        for col in range(size):
            current_row.append(f'{chr(ord("a") + col)}{size - row}')
        board.append(current_row)
    return board


size = 8
field = [input().split() for _ in range(size)]

board = create_board(size)

players_positions = {"White": (), "Black": ()}

for row in range(size):
    for col in range(size):
        if field[row][col] == "w":
            players_positions["White"] = (row, col)
        elif field[row][col] == "b":
            players_positions["Black"] = (row, col)

current_player, next_player = "White", "Black"
capture = False

while True:

    player_row, player_col = players_positions[current_player]
    if possible_attacks(player_row, player_col, current_player):
        capture = True
        break

    field[player_row][player_col] = "-"

    if current_player == "White":
        player_row -= 1
        field[player_row][player_col] = "w"
        if player_row == 0:
            break

    elif current_player == "Black":
        player_row += 1
        field[player_row][player_col] = "b"
        if player_row == size - 1:
            break

    players_positions[current_player] = (player_row, player_col)

    current_player, next_player = next_player, current_player

if capture:
    capture_row, capture_col = players_positions[next_player]
    print(f"Game over! {current_player} win, capture on {board[capture_row][capture_col]}.")

else:
    print(f"Game over! {current_player} pawn is promoted to a queen at {board[player_row][player_col]}.")
