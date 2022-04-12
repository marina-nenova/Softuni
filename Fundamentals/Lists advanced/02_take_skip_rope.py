string = list(input())

numbers_list = [el for el in string if el.isdigit()]
non_numbers_list = [el for el in string if not el.isdigit()]

take_list = [int(numbers_list[index]) for index in range(len(numbers_list)) if index % 2 == 0]
skip_list = [int(numbers_list[index]) for index in range(len(numbers_list)) if index % 2 != 0]

take_number = 0
skip_number = 0
index = 0
hidden_message = ""

for i in range(len(take_list)):
    take_number = take_list[i]
    skip_number = skip_list[i]
    hidden_message += "".join(non_numbers_list[:take_number])
    del non_numbers_list[0:take_number + skip_number]

print("".join(hidden_message))