theater_capacity = int(input())

command = input()
cinema_is_full = False
price_per_ticket = 5
total_income = 0
while command != "Movie time!":
    number_of_people = int(command)
    group_bill = number_of_people * 5
    if number_of_people % 3 == 0:
        group_bill -= 5
    theater_capacity -= number_of_people
    if theater_capacity < 0:
        cinema_is_full = True
        break
    total_income += group_bill
    command = input()

if cinema_is_full:
    print("The cinema is full.")
else:
    print(f"There are {theater_capacity} seats left in the cinema.")
print(f"Cinema income - {total_income} lv.")