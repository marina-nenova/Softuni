import re

text = input()
pattern = r"(=|\/)(?P<destination>[A-Z][A-Za-z]{2,})\1"

travel_points = 0
destinations = []

for destination in re.finditer(pattern,text):
    travel_points += len(destination.group('destination'))
    destinations.append(destination.group('destination'))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")