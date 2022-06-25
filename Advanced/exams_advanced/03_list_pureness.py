from collections import deque

def best_list_pureness(numbers_list, rotations):
    numbers = deque(numbers_list)
    rotations_count = 0
    best_pureness = 0
    for rotation in range(rotations + 1):
        current_pureness = 0
        for index in range(len(numbers)):
            current_pureness += index * numbers[index]
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            rotations_count = rotation
        numbers.rotate(1)
    return f"Best pureness {best_pureness} after {rotations_count} rotations"




test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
