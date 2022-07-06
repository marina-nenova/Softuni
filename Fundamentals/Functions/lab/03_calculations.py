def calculator(num1, num2, operator):
    if required_operation == "multiply":
        return num1 * num2
    elif required_operation == "divide":
        return int(num1 / num2)
    elif required_operation == "add":
        return num1 + num2
    elif required_operation == "subtract":
        return num1 - num2


required_operation = input()
number_1 = int(input())
number_2 = int(input())

print(calculator(number_1, number_2, required_operation))