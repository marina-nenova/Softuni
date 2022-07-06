from math import pi

figure = input()

if figure == "square":
    side = float(input())
    square_area = side ** 2
    print(f"{square_area:.3f}")
elif figure == "rectangle":
    width = float(input())
    lenght = float(input())
    rectangle_area = width * lenght
    print(f"{rectangle_area:.3f}")
elif figure == "circle":
    radius = float(input())
    circle_area = radius ** 2 * pi
    print(f"{circle_area:.3f}")
elif figure == "triangle":
    side = float(input())
    hight = float(input())
    triangle_area = (side * hight) / 2
    print(f"{triangle_area:.3f}")


