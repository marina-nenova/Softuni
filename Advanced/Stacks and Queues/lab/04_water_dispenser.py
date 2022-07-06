from collections import deque

water_available = int(input())

name = input()
line = deque()

while not name == "Start":
    line.append(name)
    name = input()
command = input()

while not command == "End":
    if command.isdigit():
        current_person = line.popleft()
        if int(command) <= water_available:
            print(f"{current_person} got water")
            water_available -= int(command)
        else:
            print(f"{current_person} must wait" )
    else:
        _, refill = command.split()
        water_available += int(refill)
    command = input()

print(f"{water_available} liters left")