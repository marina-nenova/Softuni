data = input().split(" | ")

dictionary = {}

for combination in data:
    word, definition = combination.split(": ")
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(definition)


words = input().split(" | ")

command = input()

if command == "Test":
    for word in words:
        if word in dictionary:
            print(f"{word}:")
            for definition in dictionary[word]:
                print(f" -{definition}")

elif command == "Hand Over":
    for word in dictionary:
        print(word, end=" ")