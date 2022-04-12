def target_shoot(target_number, strength, targets_list):
    if 0 <= target_number < len(targets_list):
        targets_list[target_number] -= strength
        if targets_list[target_number] <= 0:
            targets_list.pop(target_number)
    return targets_list


def insert_target(target_number, target_value, targets_list):
    if 0 <= target_number < len(targets_list):
        targets_list.insert(target_number, target_value)
        return targets_list
    else:
        print("Invalid placement!")


def strike_target(target_number, radius, targets_list):
    start = target_number - radius
    end = target_number + radius
    if start >= 0 and end < len(targets_list):
        del targets_list[start:end + 1]
        return targets_list
    else:
        print("Strike missed!")


targets = [int(el) for el in input().split()]

command = input()
while command != "End":
    data = command.split()
    target_manipulation = data[0]
    if target_manipulation == "Shoot":
        index, power = int(data[1]), int(data[2])
        target_shoot(index, power, targets)
    elif target_manipulation == "Add":
        index, value = int(data[1]), int(data[2])
        insert_target(index, value, targets)
    elif target_manipulation == "Strike":
        index, target_radius = int(data[1]), int(data[2])
        strike_target(index, target_radius, targets)
    command = input()
print(*targets, sep="|")
