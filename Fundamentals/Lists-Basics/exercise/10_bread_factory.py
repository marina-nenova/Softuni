events = input().split("|")
total_energy = 100
total_coins = 100
cannot_afford = False

for event in events:
    current_event = event.split("-")
    command = current_event[0]
    value = int(current_event[1])
    if command == "rest":
        if (total_energy + value) > 100:
            value = 100 - total_energy
        total_energy += value
        print(f"You gained {value} energy.")
        print(f"Current energy: {total_energy}.")
    elif command == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += value
            print(f"You earned {value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if value > total_coins:
            cannot_afford = True
            print(f"Closed! Cannot afford {command}.")
            break
        total_coins -= value
        print(f"You bought {command}.")

if not cannot_afford:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")

