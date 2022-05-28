from collections import deque

fireworks = deque([int(el) for el in input().split(", ")])
power = [int(el) for el in input().split(", ")]

created_fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
success = False

while fireworks and power:
    current_firework = fireworks.popleft()
    current_power = power.pop()
    if current_power <= 0 and current_firework <= 0:
        continue
    if current_power <= 0:
        fireworks.appendleft(current_firework)
        continue
    if current_firework <= 0:
        power.append(current_power)
        continue

    sum = current_firework + current_power

    if sum % 3 == 0 and sum % 5 == 0:
        created_fireworks["Crossette Fireworks"] += 1
    elif sum % 3 == 0:
        created_fireworks["Palm Fireworks"] += 1
    elif sum % 5 == 0:
        created_fireworks["Willow Fireworks"] += 1
    else:
        fireworks.append(current_firework - 1)
        power.append(current_power)
        continue
    if created_fireworks["Crossette Fireworks"] >= 3 and created_fireworks["Palm Fireworks"] >= 3 and created_fireworks["Willow Fireworks"] >= 3:
        success = True
        break

if success:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join([str(el) for el in fireworks])}")
if power:
    print(f"Explosive Power left: {', '.join([str(el) for el in power])}")

for firework, count in created_fireworks.items():
    print(f"{firework}: {count}")