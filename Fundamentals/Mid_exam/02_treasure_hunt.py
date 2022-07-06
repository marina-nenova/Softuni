initial_loot = input().split("|")

command = input()
stolen_items = []
while not command == "Yohoho!":
    data = command.split()
    action = data[0]
    if action == "Loot":
        for item in data[1:]:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif action == "Drop":
        index = int(data[1])
        if 0 <= index < len(initial_loot):
            initial_loot.append(initial_loot.pop(index))

    elif action == "Steal":
        count = int(data[1])
        if count >= len(initial_loot):
            stolen_items = initial_loot
            print(*stolen_items, sep= ", ")
            print("Failed treasure hunt.")
            initial_loot.clear()
            break
        else:
            stolen_items = initial_loot[-count:]
            del initial_loot[-count:]
            print(*stolen_items, sep=", ")

    command = input()

if len(initial_loot) > 0:
    items_length = [len(loot) for loot in initial_loot]
    treasure_gain = sum(items_length) / len(initial_loot)
    print(f"Average treasure gain: {treasure_gain:.2f} pirate credits.")
