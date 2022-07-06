from collections import deque


def calculation(numbers_collection, operation_sign):
    result = numbers_collection.popleft()
    if operation_sign == "/":
        operation_sign = "//"
    while numbers_collection:
        result += operation_sign + numbers_collection.popleft()
    return str(eval(result))


sequence = deque(input().split())
numbers = deque()

while sequence:
    current = sequence.popleft()
    if current in "+-*/":
        operation = current
        numbers.append(calculation(numbers, operation))
    else:
        numbers.append(current)

print(*numbers)
