# from collections import deque
#
# flowers = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
# found_word = ""
# success = False
#
# vowels = deque(input().split())
# consonants = input().split()
#
# while vowels and consonants:
#     vowel = vowels.popleft()
#     consonant = consonants.pop()
#
#     for flower in flowers:
#         flowers[flower] = flowers[flower].replace(vowel, "")
#         flowers[flower] = flowers[flower].replace(consonant, "")
#
#         if flowers[flower] == "":
#             found_word = flower
#             success = True
#             break
#
#     if success:
#         break
#
# if not success:
#     print("Cannot find any word!")
# else:
#     print(f"Word found: {found_word}")
#
# if vowels:
#     print(f"Vowels left: {' '.join(vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(consonants)}")


from collections import deque

vowels = deque(input().split())  # гласни
consonants = input().split()  # съгласни

flowers = {
    'rose': [],
    'tulip': [],
    'lotus': [],
    'daffodil': []
}

found_word = ''

we_have_flower = False

while vowels and consonants:
    searched_vow = vowels[0]
    searched_cons = consonants[-1]

    for flower in flowers:
        if searched_vow in flower:
            flowers[flower].append(searched_vow)
        if searched_cons in flower:
            flowers[flower].append(searched_cons)
        if len(flower) == len(flowers[flower]):
            found_word = flower
            we_have_flower = True
    searched_vow = vowels.popleft()
    searched_cons = consonants.pop()

    if we_have_flower:
        break

if we_have_flower:
    print(f'Word found: {found_word}')
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

#
# o e a o e a i
# p r r r r
