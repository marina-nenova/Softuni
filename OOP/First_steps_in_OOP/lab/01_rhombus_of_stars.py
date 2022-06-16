def print_row(row, n):
    for space in range(n - row):
        print(" ", end="")
    for row in range(1, row):
        print("*", end=" ")
    print("*")


def print_top(n):
    for row in range(1, n + 1):
        print_row(row, n)


def print_bottom(n):
    for row in range(n - 1, 0, -1):
        print_row(row, n)


def print_rombus(n):
    print_top(n)
    print_bottom(n)


n = int(input())
print_rombus(n)
