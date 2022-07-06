def index_is_valid(index):
    if 0 <= index < len(targets):
        return True

    return False


targets = list(map(int, input().split()))

command = input()

while not command == "End":
    index = int(command)
    if index_is_valid(index) and targets[index] != -1:
        target_value = targets[index]
        targets[index] = - 1
        for target_index in range(len(targets)):
            if targets[target_index] != -1 and targets[target_index] > target_value:
                targets[target_index] -= target_value
            elif targets[target_index] != -1 and targets[target_index] <= target_value:
                targets[target_index] += target_value

    command = input()

shot_targets = targets.count(-1)
targets = list(map(str, targets))
targets = " ".join(targets)
print(f"Shot targets: {shot_targets} -> {targets}")