field_rows = int(input())
ships_field = []
for i in range(field_rows):
    row = input().split()
    ships_field.append([int(el) for el in row])

attacks = input().split()

ships_destroyed = 0
for el in attacks:
    attack = el.split("-")
    row = int(attack[0])
    col = int(attack[1])
    if ships_field[row][col] > 0:
        ships_field[row][col] -= 1
        if ships_field[row][col] == 0:
            ships_destroyed += 1
print(ships_destroyed)
