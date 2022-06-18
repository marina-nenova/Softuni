def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def calculate_score(row, col, size, multiplier):
    sum_score = int(board[0][col]) + int(board[size - 1][col]) + int(board[row][0]) + int(board[row][size - 1])
    if multiplier == "D":
        return sum_score * 2
    elif multiplier == "T":
        return sum_score * 3
    elif multiplier == "B":
        return 501


size = 7
player_1, player_2 = input().split(", ")
board = [input().split() for _ in range(size)]

players_scores = {player_1: 501, player_2: 501}
players_throws = {player_1: 0, player_2: 0}

current_player, next_player = player_1, player_2
winner = ""

while True:

    throw_row, throw_col = eval(input())
    players_throws[current_player] += 1

    if valid_coordinates(throw_row, throw_col, size):

        if board[throw_row][throw_col].isdigit():
            players_scores[current_player] -= int(board[throw_row][throw_col])

        else:
            multiplier = board[throw_row][throw_col]
            score = calculate_score(throw_row, throw_col, size, multiplier)
            players_scores[current_player] -= score

        if players_scores[current_player] <= 0:
            winner = current_player
            break

    current_player, next_player = next_player, current_player

print(f"{winner} won the game with {players_throws[winner]} throws!")