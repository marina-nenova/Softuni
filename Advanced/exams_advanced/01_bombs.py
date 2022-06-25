from collections import deque

bomb_effects = deque([int(el) for el in input().split(", ")])
bomb_casings = [int(el) for el in input().split(", ")]

bombs = {40: "Datura Bombs", 60: "Cherry Bombs", 120: "Smoke Decoy Bombs"}
bombs_created = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
filled_pouch = False

while bomb_effects and bomb_casings:
    current_bomb_effect = bomb_effects.popleft()
    current_bomb_casing = bomb_casings.pop()
    current_sum = current_bomb_effect + current_bomb_casing

    if current_sum in bombs:
        current_bomb = bombs[current_sum]
        bombs_created[current_bomb] += 1
    else:
        bomb_casings.append(current_bomb_casing - 5)
        bomb_effects.appendleft(current_bomb_effect)

    if bombs_created["Datura Bombs"] >= 3 and bombs_created["Cherry Bombs"] >= 3 and bombs_created["Smoke Decoy Bombs"] >= 3:
        filled_pouch = True
        break

if filled_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects])}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(el) for el in bomb_casings])}")

for bomb, quantity in sorted(bombs_created.items()):
    print(f"{bomb}: {quantity}")