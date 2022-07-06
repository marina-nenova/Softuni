destination = input()
type_of_package = input()
vip_discount = input()
number_of_days = int(input())
price_per_day = 0
invalid_input = False

if destination in "Bansko Borovets":
    if type_of_package == "withEquipment":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day -= price_per_day * 0.1
    elif type_of_package == "noEquipment":
        price_per_day = 80
        if vip_discount == "yes":
            price_per_day -= price_per_day * 0.05
    else:
        invalid_input = True
elif destination in "Varna Burgas":
    if type_of_package == "withBreakfast":
        price_per_day = 130
        if vip_discount == "yes":
            price_per_day -= price_per_day * 0.12
    elif type_of_package == "noBreakfast":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day -= price_per_day * 0.07
    else:
        invalid_input = True
else:
    invalid_input = True

if invalid_input:
    print("Invalid input!")
elif number_of_days <= 0:
    print("Days must be positive number!")
else:
    total = price_per_day * number_of_days
    if number_of_days > 7:
        total -= price_per_day
    print(f"The price is {total:.2f}lv! Have a nice time!")