def characters_in_range(char_1, char_2):
    for symbol in range(ord(char_1) + 1, ord(char_2)):
        print(chr(symbol), end = " ")


character_1 = input()
character_2 = input()
characters_in_range(character_1, character_2)