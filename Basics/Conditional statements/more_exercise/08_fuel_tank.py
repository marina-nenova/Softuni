fuel = input()

if fuel != "Diesel" and fuel != "Gasoline" and fuel != "Gas":
    print("Invalid fuel!")

else:
    in_tank = int(input())
    if in_tank >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")
