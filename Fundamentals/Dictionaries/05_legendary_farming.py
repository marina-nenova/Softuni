legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
item_obtained = ""

while item_obtained == "":
    materials = [el.lower() for el in input().split()]
    for index in range(0, len(materials), 2):
        quantity = int(materials[index])
        material = materials[index + 1]

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                key_materials[material] -= 250
                item_obtained = legendary_items[material]
                break
        else:
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] += quantity


print(f"{item_obtained} obtained!")

for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")

for material, quantity in junk.items():
    print(f"{material}: {quantity}")
