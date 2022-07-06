def index_is_valid(index_number):
    if 0 <= index_number < len(list_of_numbers):
        return True
    return False


def check_for_matches(type):
    if type == "even":
        if sum(map(lambda x: x % 2 == 0, list_of_numbers)) > 0:
            return True
        return False
    elif type == "odd":
        if sum(map(lambda x: x % 2 != 0, list_of_numbers)) > 0:
            return True
        return False


def get_index(action, number_type):
    num = 0
    if action == "max":
        if number_type == "even":
            num = max([num for num in list_of_numbers if num % 2 == 0])
        elif number_type == "odd":
            num = max([num for num in list_of_numbers if num % 2 != 0])
    elif action == "min":
        if number_type == "even":
            num = min([num for num in list_of_numbers if num % 2 == 0])
        elif number_type == "odd":
            num = min([num for num in list_of_numbers if num % 2 != 0])
    num_index = [ind for ind in range(len(list_of_numbers) - 1, -1, -1) if list_of_numbers[ind] == num]
    return num_index[0]


def sort_list(action, number_type, count):
    sorted_list = []
    if number_type == "even":
        sorted_list = [num for num in list_of_numbers if num % 2 == 0]
    elif number_type == "odd":
        sorted_list = [num for num in list_of_numbers if num % 2 != 0]
    if count > len(sorted_list) - 1:
        return sorted_list
    else:
        if action == "first":
            sorted_list = sorted_list[:count]
        elif action == "last":
            sorted_list = sorted_list[-count:]
    return sorted_list


list_of_numbers = list(map(int, input().split()))
command = input()

while not command == "end":
    data = command.split()
    action = data[0]

    if action == "exchange":
        index = int(data[1])
        if index_is_valid(index):
            list_of_numbers = list_of_numbers[index + 1:] + list_of_numbers[:index + 1]
        else:
            print("Invalid index")

    elif action in "max min":
        number_type = data[1]
        if check_for_matches(number_type):
            print(get_index(action, number_type))
        else:
            print("No matches")

    elif action in "first last":
        count = int(data[1])
        number_type = data[2]
        if count > len(list_of_numbers):
            print("Invalid count")
        else:
            print(sort_list(action, number_type, count))

    command = input()

print(list_of_numbers)
