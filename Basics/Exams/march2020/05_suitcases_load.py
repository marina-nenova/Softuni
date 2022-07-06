plane_capacity = float(input())

command = input()
suitcase_counter = 0
plane_full = False
while command != "End":
    suitcase_volume = float(command)
    suitcase_counter += 1
    if suitcase_counter % 3 == 0:
        suitcase_volume += suitcase_volume * 0.1
    plane_capacity -= suitcase_volume
    if plane_capacity < 0:
        suitcase_counter -= 1
        plane_full = True
        break
    command = input()

if plane_full:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {suitcase_counter} suitcases loaded.")