import sys
from math import floor
the_most_powerful_word = ""
word_strength = - sys.maxsize
vowels = "aeiouy"
command = input()

while command != "End of words":
    word = command
    sum_letters = 0
    for letter in word:
        sum_letters += ord(letter)
    if word[0].lower() in vowels:
        sum_letters = sum_letters * len(word)
    else:
        sum_letters = floor(sum_letters / len(word))
    if sum_letters > word_strength:
        word_strength = sum_letters
        the_most_powerful_word = word
    command = input()
print(f"The most powerful word is {the_most_powerful_word} - {word_strength}")