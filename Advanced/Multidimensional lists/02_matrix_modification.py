def valid_coordinates(row_index, col_index):
    return 0 <= row_index < rows and 0 <= col_index < rows


rows = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

command = input()

while not command == "END":
    data = command.split()
    action = data[0]
    row = int(data[1])
    col = int(data[2])
    value = int(data[3])
    if not valid_coordinates(row, col):
        print("Invalid coordinates")
    elif action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value
    command = input()

for row in matrix:
    print(*row)