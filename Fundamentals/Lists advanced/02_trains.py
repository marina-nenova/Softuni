wagons = int(input())

train = [0] * wagons

command = input()

while not command == "End":
    data = command.split()
    action = data[0]
    if action == "add":
        train[-1] += int(data[1])
    elif action == "insert":
        wagon_number = int(data[1])
        number_of_people = int(data[2])
        train[wagon_number] += number_of_people
    elif action == "leave":
        wagon_number = int(data[1])
        number_of_people = int(data[2])
        train[wagon_number] -= number_of_people
    command = input()
print(train)