month = input()
number_of_nights = int(input())
studio_price = 0
apartment_price = 0
studio_discount = 0
apartment_discount = 0


if month in "May October":
    studio_price = 50
    apartment_price = 65
    if 7 < number_of_nights <= 14:
        studio_discount = 0.05
    elif number_of_nights > 14:
        studio_discount = 0.3
        apartment_discount = 0.1

elif month in "June September":
    studio_price = 75.2
    apartment_price = 68.7
    if number_of_nights > 14:
        studio_discount = 0.2
        apartment_discount = 0.1


elif month in "July August":
    studio_price = 76
    apartment_price = 77
    if number_of_nights > 14:
        apartment_discount = 0.1

studio_total = studio_price * number_of_nights - ((studio_price * number_of_nights) * studio_discount)
apartment_total = apartment_price * number_of_nights - ((apartment_price * number_of_nights) * apartment_discount)

print(f"Apartment: {apartment_total:.2f} lv.")
print(f"Studio: {studio_total:.2f} lv.")
