n = int(input())

numbers_stack = []

for _ in range(n):
    command = input().split()
    action = command[0]
    if action == "1":
        number = int(command[1])
        numbers_stack.append(number)
    if len(numbers_stack) > 0:
        if action == "2":
            numbers_stack.pop()
        elif action == "3":
            print(max(numbers_stack))
        elif action == "4":
            print(min(numbers_stack))


while numbers_stack:
    element = numbers_stack.pop()
    if numbers_stack:
        print(element, end=", ")
    else:
        print(element)
