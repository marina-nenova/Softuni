def valid_coordinates(row_index, col_index):
    return 0 <= row_index < size and 0 <= col_index < size


def next_position(row, col, direction):
    queen_new_positions = []

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

        if not valid_coordinates(row, col) or chess_board[row][col] == "Q":
            break
        else:
            queen_new_positions.append((row, col))
    return queen_new_positions


size = 8

chess_board = [input().split() for _ in range(size)]

queen_positions = []
king_position = ()

for row in range(size):
    for col in range(size):
        if chess_board[row][col] == "Q":
            queen_positions.append((row, col))
        elif chess_board[row][col] == "K":
            king_position = (row, col)

possible_moves = ["up left", "up", "up right", "right", "left", "down", "down right", "down left"]
successful_queens = []

for queen_row, queen_col in queen_positions:
    for direction in possible_moves:
        next_coordinates = next_position(queen_row, queen_col, direction)
        if king_position in next_coordinates:
            successful_queens.append([queen_row, queen_col])
            break

if successful_queens:
    for queen in successful_queens:
        print(queen)

else:
    print("The king is safe!")
