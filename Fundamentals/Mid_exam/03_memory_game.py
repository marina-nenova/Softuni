def index_is_valid(ind):
    if 0 <= ind < len(elements):
        return True
    else:
        return False


elements = input().split()
command = input()
moves = 0
you_won = False
while not command == "end":
    indices = command.split()
    index_1, index_2 = int(indices[0]), int(indices[1])
    moves += 1
    if index_1 == index_2 or not index_is_valid(index_1) or not index_is_valid(index_2):
        print("Invalid input! Adding additional elements to the board")
        middle = int(len(elements) / 2)
        element = "-" + str(moves) + "a"
        elements[middle:middle] = [element, element]
    elif elements[index_1] == elements[index_2]:
        matching_element = elements[index_1]
        print(f"Congrats! You have found matching elements - {matching_element}!")
        elements = [el for el in elements if el != matching_element]
    elif elements[index_1] != elements[index_2]:
        print("Try again!")
    if len(elements) == 0:
        you_won = True
        break
    command = input()

if you_won:
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    print(*elements)
