from project.controller import Controller

controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "Test"))
print(controller.add_aquarium("SaltwaterAquarium", "Test2"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Ornament"))
print(controller.insert_decoration("Test", "Ornament"))
print(controller.insert_decoration("Test2", "Plant"))
print(controller.add_fish("Test", "FreshwaterFish", "Nemo", "Clown", 5))
print(controller.add_fish("Test", "FreshwaterFish", "Marvin", "Clown", 15))
print(controller.add_fish("Test2", "SaltwaterFish", "Dori", "Bluefin", 10))
print(controller.add_fish("Test2", "SaltwaterFish", "Gill", "Moorish Idol", 20))
print(controller.feed_fish("Test2"))
print(controller.calculate_value("Test"))
print(controller.calculate_value("Test2"))
print(controller.report())

# Output
#
# Successfully added FreshwaterAquarium.
# Successfully added SaltwaterAquarium.
# Successfully added Plant.
# Successfully added Ornament.
# Successfully added Ornament to Test.
# Successfully added Plant to Test2.
# Successfully added FreshwaterFish to Test.
# Successfully added FreshwaterFish to Test.
# Successfully added SaltwaterFish to Test2.
# Successfully added SaltwaterFish to Test2.
# Fish fed: 2
# The value of Aquarium Test is 25.00.
# The value of Aquarium Test2 is 40.00.
# Test:
# Fish: Nemo Marvin
# Decorations: 1
# Comfort: 1
# Test2:
# Fish: Dori Gill
# Decorations: 1
# Comfort: 5
