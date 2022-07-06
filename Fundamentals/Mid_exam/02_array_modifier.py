numbers = [int(el) for el in input().split()]

command = input()

while not command == "end":
    data = command.split()
    action = data[0]
    if action == "swap":
        index1, index2 = int(data[1]), int(data[2])
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif action == "multiply":
        index1, index2 = int(data[1]), int(data[2])
        numbers[index1] = numbers[index1] * numbers[index2]
    elif action == "decrease":
        numbers = [num - 1 for num in numbers]
    command = input()

print(*numbers, sep=", ")
