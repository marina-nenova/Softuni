from project.planet.planet import Planet
from project.space_station import SpaceStation

space_station = SpaceStation()
print(space_station.add_astronaut("Biologist", "Peter"))
print(space_station.add_astronaut("Meteorologist", "George"))
print(space_station.add_astronaut("Geodesist", "Sam"))
print(space_station.add_planet("Mars", "coal, gold, iron, water, diamonds, silver, platinum, zinc, uranium, aluminum"))

print(space_station.send_on_mission("Mars"))
print(space_station.report())