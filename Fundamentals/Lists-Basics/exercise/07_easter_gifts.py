gifts = input().split()
command = input()

while not command == "No Money":
    data = command.split()
    action = data[0]
    gift = data[1]
    if action == "OutOfStock":
        gifts = ["None"if item == gift else item for item in gifts ]
    elif action == "Required":
        index = int(data[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif action == "JustInCase":
        gifts[-1] = gift
    command = input()

final_gifts_list = [gift for gift in gifts if gift != "None"]
print(" ".join(final_gifts_list))


# gifts = input().split(" ")
#
# while True:
#     command = input()
#     if command == "No Money":
#         break
#     command_list = command.split(" ")
#     if "OutOfStock" in command:
#         if command_list[1] in gifts:
#             for index, value in enumerate(gifts):
#                 if value == command_list[1]:
#                     gifts[index] = "None"
#     elif "Required" in command:
#         if 0 <= int(command_list[2]) < len(gifts):
#             gifts[int(command_list[2])] = command_list[1]
#     elif "JustInCase" in command:
#         gifts.pop()
#         gifts.append(command_list[1])
#
# while "None" in gifts:
#     gifts.remove("None")
#
# print(" ".join(gifts))