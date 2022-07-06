number_of_juniors = int(input())
number_of_seniors = int(input())
type_of_race = input()

juniors_fee = 0
seniors_fee = 0
if type_of_race == "trail":
    juniors_fee = 5.5
    seniors_fee = 7

elif type_of_race == "cross-country":
    juniors_fee = 8
    seniors_fee = 9.5
    if number_of_seniors + number_of_juniors >= 50:
        juniors_fee -= juniors_fee * 0.25
        seniors_fee -= seniors_fee * 0.25

elif type_of_race == "downhill":
    juniors_fee = 12.25
    seniors_fee = 13.75

elif type_of_race == "road":
    juniors_fee = 20
    seniors_fee = 21.5

total = (number_of_juniors * juniors_fee + number_of_seniors * seniors_fee) * 0.95

print(f"{total:.2f}")