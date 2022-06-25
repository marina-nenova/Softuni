# def valid_coordinates(row_index, col_index, size):
#     return 0 <= row_index < size and 0 <= col_index < size
#
#
# def calculate_score(row, col, size, multiplier):
#     sum_score = int(board[0][col]) + int(board[size - 1][col]) + int(board[row][0]) + int(board[row][size - 1])
#     if multiplier == "D":
#         return sum_score * 2
#     elif multiplier == "T":
#         return sum_score * 3
#     elif multiplier == "B":
#         return 501
#
#
# size = 7
# player_1, player_2 = input().split(", ")
# board = [input().split() for _ in range(size)]
#
# players_scores = {player_1: 501, player_2: 501}
# players_throws = {player_1: 0, player_2: 0}
#
# current_player, next_player = player_1, player_2
# winner = ""
#
# while True:
#
#     throw_row, throw_col = eval(input())
#     players_throws[current_player] += 1
#
#     if valid_coordinates(throw_row, throw_col, size):
#
#         if board[throw_row][throw_col].isdigit():
#             players_scores[current_player] -= int(board[throw_row][throw_col])
#
#         else:
#             multiplier = board[throw_row][throw_col]
#             score = calculate_score(throw_row, throw_col, size, multiplier)
#             players_scores[current_player] -= score
#
#         if players_scores[current_player] <= 0:
#             winner = current_player
#             break
#
#     current_player, next_player = next_player, current_player
#
# print(f"{winner} won the game with {players_throws[winner]} throws!")


def sums(row, col, current_field):
    result = 0
    if current_field == "D":
        result = (board[0][col] + board[-1][col] + board[row][0] + board[row][-1]) * 2
        return result
    elif current_field == "T":
        result = (board[0][col] + board[-1][col] + board[row][0] + board[row][-1]) * 3
        return result
    elif current_field == "B":
        result = 501
        return result
    else:
        result = current_field
        return result


def is_inside(row, col, s):
    return 0 <= row < s and 0 <= col < s


size = 7
first, second = input().split(", ")
first_player_points = 501
second_player_points = 501
first_player_throws = 0
second_player_throws = 0
board = []

for _ in range(size):
    board_elements = [int(x) if x != "D" and x != "T" and x != "B" else x for x in input().split()]
    board.append(board_elements)

while first_player_points > 0 and second_player_points > 0:
    coordinates = input().replace("(", "")
    coordinates = coordinates.replace(")", "")
    row_hit, col_hit = [int(x) for x in coordinates.split(", ")]

    if is_inside(row_hit, col_hit, size):
        field = board[row_hit][col_hit]
        total = sums(row_hit, col_hit, field)
        first_player_throws += 1
        first_player_points -= total
    else:
        first_player_throws += 1

    first, second = second, first
    first_player_points, second_player_points = second_player_points, first_player_points
    first_player_throws, second_player_throws = second_player_throws, first_player_throws

first, second = second, first
first_player_points, second_player_points = second_player_points, first_player_points
first_player_throws, second_player_throws = second_player_throws, first_player_throws
print(f"{first} won the game with {first_player_throws} throws!")