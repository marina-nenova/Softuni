def valid_coordinates(row_index, col_index):
    return 0 <= row_index < rows and 0 <= col_index < rows


def attack(row, col):
    attacks = 0
    possible_moves = [(row - 1, col - 2), (row - 2, col - 1), (row - 2, col + 1), (row - 1, col + 2),
                      (row + 1, col - 2), (row + 2, col - 1), (row + 2, col + 1), (row + 1, col + 2)]
    for move in possible_moves:
        row_index, col_index = move[0], move[1]
        if valid_coordinates(row_index, col_index) and board[row_index][col_index] == "K":
            attacks += 1
    return attacks


def knight_moves():
    maximum_attacks = 0
    knight_position = ()
    for row in range(rows):
        for col in range(rows):
            if board[row][col] == "K":
                attacks = attack(row, col)
                if attacks > maximum_attacks:
                    maximum_attacks = attacks
                    knight_position = (row, col)
    return knight_position, maximum_attacks


rows = int(input())

board = [list(input()) for _ in range(rows)]
knights_count = 0

while True:
    knight, maximum_attacks = knight_moves()
    if maximum_attacks == 0:
        break
    else:
        board[knight[0]][knight[1]] = "0"
        knights_count += 1

print(knights_count)