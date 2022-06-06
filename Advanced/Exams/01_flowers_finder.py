from collections import deque

flowers = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
found_word = ""
success = False

vowels = deque(input().split())
consonants = input().split()

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for flower in flowers:
        flowers[flower] = flowers[flower].replace(vowel, "")
        flowers[flower] = flowers[flower].replace(consonant, "")

        if flowers[flower] == "":
            found_word = flower
            success = True
            break

    if success:
        break

if not success:
    print("Cannot find any word!")
else:
    print(f"Word found: {found_word}")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")