def valid_coordinates(row_index, col_index):
    return 0 <= row_index < size and 0 <= col_index < size


def queen_search(row, col, direction):
    queen_position = []

    while True:
        if direction == "up left":
            row, col = row - 1, col - 1
        elif direction == "up":
            row, col = row - 1, col
        elif direction == "up right":
            row, col = row - 1, col + 1
        elif direction == "right":
            row, col = row, col + 1
        elif direction == "left":
            row, col = row + 1, col - 1
        elif direction == "down":
            row, col = row + 1, col
        elif direction == "down right":
            row, col = row + 1, col + 1
        elif direction == "down left":
            row, col = row, col - 1
        if not valid_coordinates(row, col):
            break
        elif chess_board[row][col] == "Q":
            queen_position = [row, col]
            break

    return queen_position


size = 8

chess_board = [input().split() for _ in range(size)]

queen_position = []
king_row = 0
king_col = 0

for row in range(size):
    for col in range(size):
        if chess_board[row][col] == "K":
            king_row, king_col = row, col

possible_moves = ["up left", "up", "up right", "right", "left", "down", "down right", "down left"]
successful_queens = []

for direction in possible_moves:
    queen_position = queen_search(king_row, king_col, direction)
    if queen_position:
        successful_queens.append(queen_position)

if successful_queens:
    print(*successful_queens, sep="\n")

else:
    print("The king is safe!")
