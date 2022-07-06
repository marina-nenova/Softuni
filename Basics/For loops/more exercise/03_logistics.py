number_of_cargos = int(input())
minibus = 0
truck = 0
train = 0
minibus_price = 200
truck_price = 175
train_price = 120
total_weight = 0
for cargo in range(number_of_cargos):
    weight = int(input())
    total_weight += weight
    if weight <= 3:
        minibus += weight
    elif 4 <= weight <= 11:
        truck += weight
    elif weight >= 12:
        train += weight
minibus_total = minibus * minibus_price
truck_total = truck * truck_price
train_total = train * train_price
average_price_per_ton = (minibus_total + truck_total + train_total) / total_weight
minibus_percent = (minibus / total_weight) * 100
truck_percent = (truck / total_weight) * 100
train_percent = (train / total_weight) * 100
print(f"{average_price_per_ton:.2f}")
print(f"{minibus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")