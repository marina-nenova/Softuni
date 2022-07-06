word = input()

while not word == "end":
    print(f"{word} = {word[::-1]}")
    word = input()