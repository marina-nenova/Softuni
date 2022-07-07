def even_parameters(function):
    def wrapper(*args):
        try:
            if all([el % 2 == 0 for el in args]):
                return function(*args)
            return "Please use only even numbers!"
        except TypeError:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
