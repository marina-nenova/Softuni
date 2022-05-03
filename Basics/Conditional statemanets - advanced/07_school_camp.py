season = input()
type_group = input()
number_of_students = int(input())
number_of_nights = int(input())

type_sport = ""
price_per_night = 0

if season == "Winter":
    if type_group == "girls":
        price_per_night = 9.6
        type_sport = "Gymnastics"
    elif type_group == "boys":
        price_per_night = 9.6
        type_sport = "Judo"
    elif type_group == "mixed":
        price_per_night = 10
        type_sport = "Ski"

elif season == "Spring":
    if type_group == "girls":
        price_per_night = 7.2
        type_sport = "Athletics"
    elif type_group == "boys":
        price_per_night = 7.2
        type_sport = "Tennis"
    elif type_group == "mixed":
        price_per_night = 9.5
        type_sport = "Cycling"

elif season == "Summer":
    if type_group == "girls":
        price_per_night = 15
        type_sport = "Volleyball"
    elif type_group == "boys":
        price_per_night = 15
        type_sport = "Football"
    elif type_group == "mixed":
        price_per_night = 20
        type_sport = "Swimming"

total = number_of_students * price_per_night * number_of_nights

if 10 <= number_of_students < 20:
    total -= total * 0.05
elif 20 <= number_of_students < 50:
    total -= total * 0.15
elif number_of_students >= 50:
    total -= total * 0.5

print(f"{type_sport} {total:.2f} lv.")

