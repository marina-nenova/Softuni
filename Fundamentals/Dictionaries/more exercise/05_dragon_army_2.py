class Dragon:
    def __init__(self, name, damage, health, armor):
        self.name = name
        if damage == "null":
            self.damage = 45
        else:
            self.damage = int(damage)
        if health == "null":
            self.health = 250
        else:
            self.health = int(health)
        if armor == "null":
            self.armor = 10
        else:
            self.armor = int(armor)


num = int(input())
dragons = {}

for _ in range(num):
    type_dragon, name, damage, health, armor = input().split()
    dragon = Dragon(name, damage, health, armor)

    if type_dragon not in dragons:
        dragons[type_dragon] = []

    for dragon_info in dragons[type_dragon]:
        if dragon_info.name == name:
            dragons[type_dragon].remove(dragon_info)

    dragons[type_dragon].append(dragon)


for type, dragons_info in dragons.items():
    average_damage = sum([i.damage for i in dragons_info]) / len(dragons_info)
    average_health = sum([i.num_collection for i in dragons_info]) / len(dragons_info)
    average_armor = sum([i.armor for i in dragons_info]) / len(dragons_info)
    print(f"{type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    for dragon in sorted(dragons_info, key=lambda d: d.name):
        print(f"-{dragon.name} -> damage: {dragon.damage}, health: {dragon.num_collection}, armor: {dragon.armor}")
