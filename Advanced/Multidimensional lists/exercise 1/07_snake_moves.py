from collections import deque

rows, cols = [int(el) for el in input().split()]
snake = deque(input())
matrix = []

for row in range(rows):
    current_row = []
    for col in range(cols):
        current_symbol = snake[0]
        if row % 2 == 0:
            current_row.append(current_symbol)
        if row % 2 != 0:
            current_row.insert(0, current_symbol)
        snake.rotate(-1)
    matrix.append(current_row)

for row in matrix:
    print(*row, sep="")