def check_coordinates(num_list):
    if 0 <= int(num_list[0]) < rows and 0 <= int(num_list[1]) < cols and 0 <= int(num_list[2]) < rows and 0 <= int(num_list[3]) < cols:
        return True
    return False


rows, cols = [int(el) for el in input().split()]
matrix = []

for _ in range(rows):
    line = input().split()
    matrix.append(line)

command = input()

while not command == "END":
    data = command.split()
    coordinates = data[1:]
    if data[0] == "swap" and len(data) == 5 and check_coordinates(coordinates):
        row1 = int(coordinates[0])
        col1 = int(coordinates[1])
        row2 = int(coordinates[2])
        col2 = int(coordinates[3])
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in matrix:
            print(*row)
    else:
        print("Invalid input!")
    command = input()
