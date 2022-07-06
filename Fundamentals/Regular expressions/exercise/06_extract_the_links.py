import re

text = input()
pattern = r"([w]{3}\.[A-Za-z0-9-]+(?:\.[9a-z]+)+)"
valid_links = []
while text:
    matches = re.findall(pattern, text)
    if matches:
        valid_links.append(matches[0])
    text = input()

print(*valid_links, sep="\n")