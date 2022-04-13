characters = input().split(", ")

dictionary = {char: ord(char) for char in characters}

print(dictionary)