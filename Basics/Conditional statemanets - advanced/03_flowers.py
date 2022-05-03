number_of_chrysanthemum = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
holiday = input()

chrysanthemum_price = 0
roses_price = 0
tulips_price = 0
if season in "Spring Summer":
    chrysanthemum_price = 2
    roses_price = 4.1
    tulips_price = 2.5
elif season in "Autumn Winter":
    chrysanthemum_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15

price_flowers = number_of_chrysanthemum * chrysanthemum_price + number_of_roses * roses_price + number_of_tulips * tulips_price

if holiday == "Y":
    price_flowers += price_flowers * 0.15

if season == "Spring" and number_of_tulips > 7:
    price_flowers -= price_flowers * 0.05
elif season == "Winter" and number_of_roses >= 10:
    price_flowers -= price_flowers * 0.1

if number_of_roses + number_of_chrysanthemum + number_of_tulips > 20:
    price_flowers -= price_flowers * 0.2

total = price_flowers + 2
print(f"{total:.2f}")
