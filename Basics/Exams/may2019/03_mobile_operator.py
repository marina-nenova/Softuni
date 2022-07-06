mobile_plan_duration = input()
type_of_mobile_plan = input()
mobile_data = input()
number_of_months = int(input())
monthly_fee = 0
if mobile_plan_duration == "one":
    if type_of_mobile_plan == "Small":
        monthly_fee = 9.98
    elif type_of_mobile_plan == "Middle":
        monthly_fee = 18.99
    elif type_of_mobile_plan == "Large":
        monthly_fee = 25.98
    elif type_of_mobile_plan == "ExtraLarge":
        monthly_fee = 35.99
elif mobile_plan_duration == "two":
    if type_of_mobile_plan == "Small":
        monthly_fee = 8.58
    elif type_of_mobile_plan == "Middle":
        monthly_fee = 17.09
    elif type_of_mobile_plan == "Large":
        monthly_fee = 23.59
    elif type_of_mobile_plan == "ExtraLarge":
        monthly_fee = 31.79

if mobile_data == "yes":
    if monthly_fee <= 10:
        monthly_fee += 5.5
    elif monthly_fee <= 30:
        monthly_fee += 4.35
    elif monthly_fee > 30:
        monthly_fee += 3.85
total = monthly_fee * number_of_months

if mobile_plan_duration == "two":
    total -= total * 0.0375
print(f"{total:.2f} lv.")