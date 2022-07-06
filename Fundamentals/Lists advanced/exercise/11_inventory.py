# def item_already_exists(item, items_list):
#     if item in items_list:
#         return True
#     return False
#
#
# list_of_items = input().split(", ")
# command = input()
#
# while not command == "Craft!":
#     data = command.split(" - ")
#     action = data[0]
#     item_name = data[1]
#     if action == "Collect":
#         if not item_already_exists(item_name, list_of_items):
#             list_of_items.append(item_name)
#     elif action == "Drop":
#         if item_already_exists(item_name, list_of_items):
#             list_of_items.remove(item_name)
#     elif action == "Combine Items":
#         old_item, new_item = data[1].split(":")
#         if item_already_exists(old_item, list_of_items):
#             old_item_index = list_of_items.index(old_item)
#             list_of_items.insert(old_item_index + 1, new_item)
#     elif action == "Renew":
#         if item_already_exists(item_name, list_of_items):
#             list_of_items.remove(item_name)
#             list_of_items.append(item_name)
#     command = input()
#
# print(", ".join(list_of_items))


def collect_function(data, item):
    if item not in data:
        data.append(item)
    return data


def drop_function(data, item):
    if item in data:
        data.remove(item)
    return data


def combine_items_function(data, items):
    items = items.split(':')
    old = items[0]
    new = items[1]

    if old in data:
        index_old = data.index(old)
        data.insert(index_old + 1, new)
    return data


def renew_function(data, item):
    if item in data:
        data.remove(item)
        data.append(item)
    return data



def inventory(data):
    while True:
        command = input().split(' - ')

        if command[0] == 'Craft!':
            print(', '.join(data))
            break
        current_command = command[0]
        items = command[1]

        if current_command == 'Collect':
            data = collect_function(data, items)
        elif current_command == 'Drop':
            data = drop_function(data, items)
        elif current_command == 'Combine Items':
            data = combine_items_function(data, items)
        elif current_command == 'Renew':
            data = renew_function(data, items)


info = input().split(', ')
inventory(info)
