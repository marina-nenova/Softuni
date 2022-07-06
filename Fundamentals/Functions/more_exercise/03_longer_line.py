import math


def line_length(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    line_1_length = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    line_2_length = math.sqrt((x_4 - x_3) ** 2 + (y_4 - y_3) ** 2)
    if line_1_length >= line_2_length:
        distance_calculator(x_1, y_1, x_2, y_2)
    else:
        distance_calculator(x_3, y_3, x_4, y_4)


def distance_calculator(x, y, z, p):
    if x ** 2 + y ** 2 <= z ** 2 + p ** 2:
        print(f"({math.floor(x)}, {math.floor(y)})({math.floor(z)}, {math.floor(p)})")
    else:
        print(f"({math.floor(z)}, {math.floor(p)})({math.floor(x)}, {math.floor(y)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

line_length(x1, y1, x2, y2, x3, y3, x4, y4)
