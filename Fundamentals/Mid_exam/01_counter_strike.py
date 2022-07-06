energy = int(input())

command = input()
battles_won = 0
not_enough_energy = False
while not command == "End of battle":
    distance = int(command)
    if energy >= distance:
        battles_won += 1
        energy -= distance
        if battles_won % 3 == 0:
            energy += battles_won
    else:
        not_enough_energy = True
        break
    command = input()

if not_enough_energy:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
else:
    print(f"Won battles: {battles_won}. Energy left: {energy}" )