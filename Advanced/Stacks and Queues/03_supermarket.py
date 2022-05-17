from collections import deque

command = input()
line = deque()

while not command == "End":
    if command == "Paid":
        while line:
            print(line.popleft())
    else:
        line.append(command)
    command = input()

print(f"{len(line)} people remaining.")