from project.space_station import SpaceStation

space_station = SpaceStation()
print(space_station.add_astronaut("Biologist", "Peter"))
print(space_station.add_astronaut("Meteorologist", "George"))
print(space_station.add_astronaut("Geodesist", "Sam"))
print(space_station.add_planet("Mars", "coal, gold, iron, water, diamonds, silver, platinum, zinc, uranium, aluminum"))

print(space_station.send_on_mission("Mars"))
print(space_station.report())

# Output
#
# Successfully added Biologist: Peter.
# Successfully added Meteorologist: George.
# Successfully added Geodesist: Sam.
# Successfully added Planet: Mars.
# Planet: Mars was explored. 2 astronauts participated in collecting items.
# 1 successful missions!
# 0 missions were not completed!
# Astronauts' info:
# Name: Peter
# Oxygen: 50
# Backpack items: water, iron, gold, coal
# Name: George
# Oxygen: 0
# Backpack items: aluminum, uranium, zinc, platinum, silver, diamonds
# Name: Sam
# Oxygen: 50
# Backpack items: none