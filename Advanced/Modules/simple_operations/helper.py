def sum_nums(a, b):
    return a + b


def sub_nums(a, b):
    return a - b


def div_nums(a, b):
    return a / b


def mul_nums(a, b):
    return a * b


def pow_nums(a, b):
    return a ** b


operation_mapper = {
    "+": sum_nums,
    "-": sub_nums,
    "/": div_nums,
    "*": mul_nums,
    "^": pow_nums
}
