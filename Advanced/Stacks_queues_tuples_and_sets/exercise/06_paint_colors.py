from collections import deque

substrings = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
collected_colors = []

while substrings:
    first = substrings.popleft()
    second = substrings.pop() if substrings else ''

    result = first + second
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    result = second + first
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    first = first[:-1]
    second = second[:-1]

    if first:
        substrings.insert(len(substrings) // 2, first)
    if second:
        substrings.insert(len(substrings) // 2, second)

result = []
required_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["blue", "yellow"],
}

for color in collected_colors:
    if color in main_colors:
        result.append(color)
    elif color in secondary_colors:
        is_valid = True
        for required_color in required_colors[color]:
            if required_color not in collected_colors:
                is_valid = False
                break
        if is_valid:
            result.append(color)

print(result)