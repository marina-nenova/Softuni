name_of_movie = input()
type_of_hall = input()
number_of_tickets = int(input())
price_per_ticket = 0
if name_of_movie == "A Star Is Born":
    if type_of_hall == "normal":
        price_per_ticket = 7.50
    elif type_of_hall == "luxury":
        price_per_ticket = 10.50
    elif type_of_hall == "ultra luxury":
        price_per_ticket = 13.50
elif name_of_movie == "Bohemian Rhapsody":
    if type_of_hall == "normal":
        price_per_ticket = 7.35
    elif type_of_hall == "luxury":
        price_per_ticket = 9.45
    elif type_of_hall == "ultra luxury":
        price_per_ticket = 12.75
elif name_of_movie == "Green Book":
    if type_of_hall == "normal":
        price_per_ticket = 8.15
    elif type_of_hall == "luxury":
        price_per_ticket = 10.25
    elif type_of_hall == "ultra luxury":
        price_per_ticket = 13.25
elif name_of_movie == "The Favourite":
    if type_of_hall == "normal":
        price_per_ticket = 8.75
    elif type_of_hall == "luxury":
        price_per_ticket = 11.55
    elif type_of_hall == "ultra luxury":
        price_per_ticket = 13.95
total_income = number_of_tickets * price_per_ticket
print(f"{name_of_movie} -> {total_income:.2f} lv.")