text = input()

occurrences = {}

for char in text:
    if char != " ":
        if char not in occurrences:
            occurrences[char] = 0
        occurrences[char] += 1

for char, occurrence in occurrences.items():
    print(f"{char} -> {occurrence}")