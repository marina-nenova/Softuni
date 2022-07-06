key = int(input())
n = int(input())
message = ""

for char in range(n):
    character = input()
    letter = ord(character) + key
    message += chr(letter)
print(message)