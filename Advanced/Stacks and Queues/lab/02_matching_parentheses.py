expression = input()

indices_stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        indices_stack.append(index)
    if expression[index] == ")":
        start = indices_stack.pop()
        print(expression[start: index + 1])