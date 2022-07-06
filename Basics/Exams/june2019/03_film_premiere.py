movie = input()
movie_package = input()
number_of_tickets = int(input())

price_per_ticket = 0

if movie == "John Wick":
    if movie_package == "Drink":
        price_per_ticket = 12
    elif movie_package == "Popcorn":
        price_per_ticket = 15
    elif movie_package == "Menu":
        price_per_ticket = 19
elif movie == "Star Wars":
    if movie_package == "Drink":
        price_per_ticket = 18
    elif movie_package == "Popcorn":
        price_per_ticket = 25
    elif movie_package == "Menu":
        price_per_ticket = 30
elif movie == "Jumanji":
    if movie_package == "Drink":
        price_per_ticket = 9
    elif movie_package == "Popcorn":
        price_per_ticket = 11
    elif movie_package == "Menu":
        price_per_ticket = 14

total = price_per_ticket * number_of_tickets
if number_of_tickets >= 4 and movie == "Star Wars":
    total -= total * 0.3
elif number_of_tickets == 2 and movie == "Jumanji":
    total -= total * 0.15

print(f"Your bill is {total:.2f} leva.")

