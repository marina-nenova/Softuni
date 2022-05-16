saved_money = 0

destination = input()

while destination != "End":
    budget = float(input())
    saved_money = 0
    while saved_money < budget:
        money = float(input())
        saved_money += money
    print(f"Going to {destination}!")
    destination = input()
