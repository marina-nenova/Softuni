def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def calculate_score(row_index, col_index, multiplier_letter):
    score = int(board[0][col_index]) + int(board[6][col_index]) + int(board[row_index][0]) + int(board[row_index][6])
    if multiplier_letter == "D":
        score *= 2
    elif multiplier_letter == "T":
        score *= 3
    elif multiplier_letter == "B":
        score = 501
    return score


size = 7
first, second = input().split(", ")
board = [input().split() for _ in range(size)]

score_board = {first: 501, second: 501}
throws_count = {first: 0, second: 0}

while True:
    throw = input()
    row, col = [int(el) for el in throw[1:-1].split(", ")]

    if not valid_coordinates(row, col, size):
        throws_count[first] += 1
        first, second = second, first
        continue

    if board[row][col].isdigit():
        throw_score = int(board[row][col])
        score_board[first] -= throw_score

    else:
        multiplier_letter = board[row][col]
        score = calculate_score(row, col, multiplier_letter)
        score_board[first] -= score

    throws_count[first] += 1

    if score_board[first] <= 0:
        print(f"{first} won the game with {throws_count[first]} throws!")
        break

    first, second = second, first
