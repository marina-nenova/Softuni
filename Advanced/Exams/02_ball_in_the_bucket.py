def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def calculate_score(col_index):
    score = 0
    for row_index in range(size):
        if field[row_index][col_index].isdigit():
            score += int(field[row_index][col_index])

    return score


size = 6

field = [input().split() for _ in range(size)]
player_score = 0

for _ in range(3):
    throw_coordinates = input()
    row, col = [int(el) for el in throw_coordinates[1:-1].split(", ")]

    if valid_coordinates(row, col, size) and field[row][col] == "B":
        player_score += calculate_score(col)
        field[row][col] = 0

present = ""

if player_score < 100:
    needed_points = 100 - player_score
    print(f"Sorry! You need {needed_points} points more to win a prize.")
elif 100 <= player_score < 200:
    present = "Football"
elif 200 <= player_score < 300:
    present = "Teddy Bear"
elif player_score >= 300:
    present = "Lego Construction Set"

if present:
    print(f"Good job! You scored {player_score} points, and you've won {present}.")


# import ast
#
# size = 6
# matrix = [[x for x in input().split()] for _ in range(size)]
#
# points = 0
# prize = ''
# buckets_coords = []
#
# for _ in range(3):
#
#     coords = input()
#     row, col = ast.literal_eval(coords)
#
#     current_sum = 0
#
#     if 0 <= row < size and 0 <= col < size:
#         position = matrix[row][col]
#         if position == "B" and coords not in buckets_coords:
#             buckets_coords.append(coords)
#
#             for el in range(size):
#                 if not matrix[el][col] == 'B':
#                     current_sum += int(matrix[el][col])
#             points += current_sum
#
# if points > 99:
#     if 100 <= points <= 199:
#         prize = 'Football'
#     elif 200 <= points <= 299:
#         prize = 'Teddy Bear'
#     elif points >= 300:
#         prize = 'Lego Construction Set'
#     print(f"Good job! You scored {points} points, and you've won {prize}.")
#
# else:
#     print(f"Sorry! You need {100 - points} points more to win a prize.")
#
