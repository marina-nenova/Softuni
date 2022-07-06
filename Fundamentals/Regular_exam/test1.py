import re

text = input()
pattern = r"(?:[@]+|[#]+)(?P<color>[a-z]{3,})(?:[@]+|[#]+)[^A-Za-z0-9]*\/+(?P<quantity>\d+)\/+"

for egg in re.finditer(pattern, text):
    print(f"You found {egg.group('quantity')} {egg.group('color')} eggs!")