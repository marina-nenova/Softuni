def item_already_exists(item):
    if item in grocery_list:
        return True
    return False

grocery_list = input().split("!")

command = input()

while not command == "Go Shopping!":
    data = command.split()
    action = data[0]
    item = data[1]
    if action == "Urgent":
        if not item_already_exists(item):
            grocery_list.insert(0, item)
    elif action == "Unnecessary":
        if item_already_exists(item):
            grocery_list.remove(item)
    elif action == "Correct":
        new_item = data[2]
        if item_already_exists(item):
            old_item_index = grocery_list.index(item)
            grocery_list[old_item_index] = new_item
    elif action == "Rearrange":
        if item_already_exists(item):
            item_index = grocery_list.index(item)
            grocery_list.append(grocery_list.pop(item_index))
    command = input()

print(", ".join(grocery_list))
