def find_next(coordinates, board):
    next_coordinates = []
    if coordinates[0] - 1 >= 0 and board[coordinates[0] - 1][coordinates[1]] == ".":  # check up and if first row
        next_coordinates.append((coordinates[0] - 1, coordinates[1]))
    if coordinates[0] + 1 < len(board) and board[coordinates[0] + 1][coordinates[1]] == ".":  # check down
        next_coordinates.append((coordinates[0] + 1, coordinates[1]))
    if coordinates[1] + 1 < len(board[0]) and board[coordinates[0]][coordinates[1] + 1] == ".":  # check right
        next_coordinates.append((coordinates[0], coordinates[1] + 1))
    if coordinates[1] - 1 >= 0 and board[coordinates[0]][coordinates[1] - 1] == ".":  # check left and if first column
        next_coordinates.append((coordinates[0], coordinates[1] - 1))
    return next_coordinates


def dfs(board, stack, all_visited, sequence_visited, start):

    stack.append(start)
    all_visited.add(start)
    sequence_visited.add(start)

    while stack:
        n = stack.pop()
        next_steps = find_next(n, board)  # sends coordinate to function to find next available moves
        for x in next_steps:
            if x in sequence_visited:  # checks if visited
                continue
            all_visited.add(x)
            sequence_visited.add(x)
            stack.append(x)

    sequence_length = len(sequence_visited)
    return sequence_length


rows = int(input())
board = []
stack = []
start = ()
all_checked = set()
sequence_count = set()
largest_count = 0

for row in range(rows):
    board.append(input().split())

for row in range(rows):
    for col in range(len(board[row])):
        if board[row][col] == "." and (row, col) not in all_checked:
            start = (row, col)
            connected = dfs(board, stack, all_checked, sequence_count, start)
            if connected > largest_count:
                largest_count = connected
            sequence_count.clear()

print(largest_count)
