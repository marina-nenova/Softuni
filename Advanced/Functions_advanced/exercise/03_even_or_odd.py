def even_odd(*args):
    type = args[-1]
    parity = 0 if type == "even" else 1
    return [el for el in args[:-1] if el % 2 == parity]



print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))