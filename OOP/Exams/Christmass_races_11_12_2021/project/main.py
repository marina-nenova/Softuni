from project.controller import Controller

controller = Controller()
print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(controller.create_driver("John"))
print(controller.create_driver("Jack"))
print(controller.create_driver("Kelly"))
print(controller.add_car_to_driver("Kelly", "MuscleCar"))
print(controller.add_car_to_driver("Jack", "MuscleCar"))
print(controller.add_car_to_driver("John", "SportsCar"))
print(controller.create_race("Christmas Top Racers"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
print(controller.start_race("Christmas Top Racers"))
[print(d.name, d.number_of_wins) for d in controller.drivers]

# Output
#
# Driver Peter is created.
# SportsCar Porsche 718 Boxster is created.
# Driver Peter chose the car Porsche 718 Boxster.
# SportsCar Porsche 911 is created.
# Driver Peter changed his car from Porsche 718 Boxster to Porsche 911.
# MuscleCar BMW ALPINA B7 is created.
# MuscleCar Mercedes-Benz AMG GLA 45 is created.
# Driver John is created.
# Driver Jack is created.
# Driver Kelly is created.
# Driver Kelly chose the car Mercedes-Benz AMG GLA 45.
# Driver Jack chose the car BMW ALPINA B7.
# Driver John chose the car Porsche 718 Boxster.
# Race Christmas Top Racers is created.
# Driver John added in Christmas Top Racers race.
# Driver Jack added in Christmas Top Racers race.
# Driver Kelly added in Christmas Top Racers race.
# Driver Peter added in Christmas Top Racers race.
# Driver Peter wins the Christmas Top Racers race with a speed of 580.
# Driver John wins the Christmas Top Racers race with a speed of 470.
# Driver Kelly wins the Christmas Top Racers race with a speed of 420.
# Peter 1
# John 1
# Jack 0
# Kelly 1
