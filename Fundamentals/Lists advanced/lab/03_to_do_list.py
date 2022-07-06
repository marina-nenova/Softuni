command = input()

to_do_list = [0] * 10
while not command == "End":
    importance, action = command.split("-")
    importance_index = int(importance)
    to_do_list[importance_index] = action
    command = input()
print([el for el in to_do_list if el != 0])