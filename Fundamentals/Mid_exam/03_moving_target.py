def index_is_valid(index_number):
    if 0 <= index_number < len(targets):
        return True
    else:
        return False


targets = [int(el) for el in input().split()]

command = input()
while not command == "End":
    manipulation = command.split()
    action, index = manipulation[0], int(manipulation[1])

    if action == "Shoot":
        power = int(manipulation[2])
        if index_is_valid(index):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif action == "Add":
        value = int(manipulation[2])
        if index_is_valid(index):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = int(manipulation[2])
        start_index = index - radius
        end_index = index + radius
        if index_is_valid(start_index) and index_is_valid(end_index):
            del targets[start_index:end_index + 1]
        else:
            print("Strike missed!")
    command = input()

print(*targets, sep="|")
