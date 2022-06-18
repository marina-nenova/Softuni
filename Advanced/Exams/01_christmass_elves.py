from collections import deque

elves = deque([int(el) for el in input().split()])
materials = [int(el) for el in input().split()]

energy_used = 0
crafted_toys = 0
count = 0

while elves and materials:
    current_elf = elves.popleft()
    current_material = materials.pop()

    if current_elf < 5:
        materials.append(current_material)
        continue

    count += 1
    needed_energy = current_material

    if count % 3 == 0:
        needed_energy = current_material * 2

    if current_elf < needed_energy:
        elves.append(current_elf * 2)
        materials.append(current_material)
        continue

    energy_used += needed_energy
    current_elf -= needed_energy

    if count % 3 == 0 and count % 5 == 0:
        elves.append(current_elf)

    elif count % 3 == 0:
        elves.append(current_elf + 1)
        crafted_toys += 2

    elif count % 5 == 0:
        elves.append(current_elf)

    else:
        elves.append(current_elf + 1)
        crafted_toys += 1


print(f"Toys: {crafted_toys}")
print(f"Energy: {energy_used}")

if elves:
    print(f"Elves left: {', '.join([str(el) for el in elves])}")

if materials:
    print(f"Boxes left: {', '.join([str(el) for el in materials])}")


