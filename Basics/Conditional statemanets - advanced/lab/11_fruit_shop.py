fruit = input()
day_of_week = input()
amount = float(input())

total = 0
condition = True

if day_of_week in "Monday Tuesday Wednesday Thursday Friday":
    if fruit == "banana":
        total = amount * 2.5
    elif fruit == "apple":
        total = amount * 1.2
    elif fruit == "orange":
        total = amount * 0.85
    elif fruit == "grapefruit":
        total = amount * 1.45
    elif fruit == "kiwi":
        total = amount * 2.7
    elif fruit == "pineapple":
        total = amount * 5.5
    elif fruit == "grapes":
        total = amount * 3.85
    else:
        condition = False

elif day_of_week in "Saturday Sunday":
    if fruit == "banana":
        total = amount * 2.7
    elif fruit == "apple":
        total = amount * 1.25
    elif fruit == "orange":
        total = amount * 0.9
    elif fruit == "grapefruit":
        total = amount * 1.6
    elif fruit == "kiwi":
        total = amount * 3
    elif fruit == "pineapple":
        total = amount * 5.6
    elif fruit == "grapes":
        total = amount * 4.2
    else:
        condition = False
else:
    condition = False

if condition:
    print(f"{total:.2f}")
else:
    print("error")

