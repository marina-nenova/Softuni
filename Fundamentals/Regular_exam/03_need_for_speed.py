def drive(car, distance, fuel, max_mileage):
    if cars[car]['fuel'] < fuel:
        print("Not enough fuel to make that ride")
    else:
        cars[car]['mileage'] += distance
        cars[car]['fuel'] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]['mileage'] >= max_mileage:
            del cars[car]
            print(f"Time to sell the {car}!")


def refuel(car, fuel, tank_capacity):
    litres = fuel
    if cars[car]['fuel'] + fuel > tank_capacity:
        litres = tank_capacity - cars[car]['fuel']
    cars[car]['fuel'] += litres
    print(f"{car} refueled with {litres} liters")


def revert(car, kilometers, min_mileage):
    if cars[car]['mileage'] - kilometers < min_mileage:
        cars[car]['mileage'] = min_mileage
    else:
        cars[car]['mileage'] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")


n = int(input())

max_mileage = 100000
tank_capacity = 75
min_mileage = 10000

cars = {}

for _ in range(n):
    car, mileage, fuel = input().split("|")
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

command = input()

while not command == "Stop":
    data = command.split(" : ")
    action = data[0]
    car = data[1]
    if action == "Drive":
        distance = int(data[2])
        fuel = int(data[3])
        drive(car, distance, fuel, max_mileage)
    elif action == "Refuel":
        fuel = int(data[2])
        refuel(car, fuel, tank_capacity)
    elif action == "Revert":
        kilometers = int(data[2])
        revert(car, kilometers, min_mileage)

    command = input()

for car, info in cars.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")