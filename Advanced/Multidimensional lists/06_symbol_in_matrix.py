rows = int(input())
matrix = []

for _ in range(rows):
    line = input()
    matrix.append(list(line))

searched_symbol = input()
success = False
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == searched_symbol:
            print((row,col))
            success = True
            break
    if success:
        break

if not success:
    print(f"{searched_symbol} does not occur in the matrix")
