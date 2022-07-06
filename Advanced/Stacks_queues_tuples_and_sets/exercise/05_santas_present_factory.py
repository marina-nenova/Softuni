from collections import deque

materials = deque([int(el) for el in input().split()])
magic = deque([int(el) for el in input().split()])

presents_magic_needed = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
presents_crafted = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    if current_material == 0 and current_magic == 0:
        continue
    if current_material == 0:
        magic.appendleft(current_magic)
        continue
    if current_magic == 0:
        materials.append(current_material)
        continue

    multiplication_result = current_material * current_magic
    if multiplication_result in presents_magic_needed:
        present = presents_magic_needed[multiplication_result]
        presents_crafted[present] += 1
    elif multiplication_result < 0:
        materials.append(current_material + current_magic)
    elif multiplication_result > 0:
        materials.append(current_material + 15)

if (presents_crafted["Bicycle"] > 0 and presents_crafted["Teddy bear"] > 0)\
        or (presents_crafted["Doll"] > 0 and presents_crafted["Wooden train"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(el) for el in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(el) for el in magic)}")

for present, count in sorted(presents_crafted.items()):
    if count > 0:
        print(f"{present}: {count}")
