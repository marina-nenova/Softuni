def item_already_exists(item):
    if item in items:
        return True

    return False


items = [el for el in input().split(", ")]

command = input()
while not command == "Craft!":
    data = command.split(" - ")
    action = data[0]
    item = data[1]
    if action == "Collect":
        if not item_already_exists(item):
            items.append(item)

    elif action == "Drop":
        if item_already_exists(item):
            items.remove(item)

    elif action == "Combine Items":
        item_pairs = item.split(":")
        old_item, new_item = item_pairs[0], item_pairs[1]
        if item_already_exists(old_item):
            old_item_index = items.index(old_item)
            items.insert(old_item_index + 1, new_item)

    elif action == "Renew":
        if item_already_exists(item):
            items.remove(item)
            items.append(item)

    command = input()
print(*items, sep=", ")