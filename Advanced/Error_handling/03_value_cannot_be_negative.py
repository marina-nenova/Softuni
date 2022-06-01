class ValueCannotBeNegative(Exception):
    pass


while True:
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative