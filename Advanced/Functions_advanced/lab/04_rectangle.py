def area(length, width):
    return length * width


def perimeter(length, width):
    return length * 2 + width * 2


def rectangle(length, width):
    try:
        rect_area = area(length, width)
        rect_perim = perimeter(length, width)
        return f"Rectangle area: {rect_area}\nRectangle perimeter: {rect_perim}"
    except:
        return "Enter valid values!"


print(rectangle('2', 10))

