w = float(input())
h = float(input())

free_width = h - 1
desks_in_width = free_width // 0.7
desks_in_lenght = w // 1.2
number_of_desks = desks_in_width * desks_in_lenght - 3
print(int(number_of_desks))