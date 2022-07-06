ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

quantity = int(input())
days_until_christmas = int(input())
total = 0
christmas_spirit = 0
for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total += ornament_set_price * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        total += (tree_skirt_price + tree_garlands_price) * quantity
        christmas_spirit += 13
    if day % 5 == 0:
        total += tree_lights_price * quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        total += tree_skirt_price + tree_garlands_price + tree_lights_price
        if day == days_until_christmas:
            christmas_spirit -= 30
print(f"Total cost: {total}")
print(f"Total spirit: {christmas_spirit}")