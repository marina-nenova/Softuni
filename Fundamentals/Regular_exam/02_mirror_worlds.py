import re

text = input()
pattern = r"(@|#)(?P<first>[A-Za-z]{3,})\1\1(?P<second>[A-za-z]{3,})\1"

mirror_words = []
matches = list(re.finditer(pattern, text))

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
    for match in matches:
        word_1 = match.group('first')
        word_2 = match.group('second')
        if word_1 == word_2[::-1]:
            mirror_words.append(word_1 + " <=> " + word_2)

if mirror_words:
    print("The mirror words are:")
    print(', '.join(mirror_words))
else:
    print("No mirror words!")