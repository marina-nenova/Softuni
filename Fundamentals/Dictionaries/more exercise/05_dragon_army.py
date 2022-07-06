def convert_values(damage, health, armor):
    if damage == "null":
        damage = 45
    else:
        damage = int(damage)
    if health == "null":
        health = 250
    else:
        health = int(health)
    if armor == "null":
        armor = 10
    else:
        armor = int(armor)
    return damage, health, armor


num = int(input())
dragons = {}
for _ in range(num):
    type_dragon, name, damage, health, armor = input().split()
    damage, health, armor = convert_values(damage, health, armor)

    if type_dragon not in dragons:
        dragons[type_dragon] = {}
    dragons[type_dragon][name] = [damage, health, armor]

for type_dragon, dragon_info in dragons.items():
    average_damage = sum([i[0] for i in dragon_info.values()]) / len(dragon_info)
    average_health = sum([i[1] for i in dragon_info.values()]) / len(dragon_info)
    average_armor = sum([i[2] for i in dragon_info.values()]) / len(dragon_info)
    print(f"{type_dragon}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    for name, values in sorted(dragon_info.items(), key=lambda x: x[0]):
        print(f"-{name} -> damage: {values[0]}, health: {values[1]}, armor: {values[2]}")
