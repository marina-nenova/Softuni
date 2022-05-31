def words_sorting(*args):
    word_dict = {}
    for word in args:
        word_value = sum(ord(char) for char in word)
        word_dict[word] = word_value
    if sum(word_dict.values()) %2 != 0:
        sorted_dict = dict(sorted(word_dict.items(), key= lambda kvpt: kvpt[1], reverse=True))
    else:
        sorted_dict = dict(sorted(word_dict.items(), key= lambda kvpt: kvpt[0]))

    output = ""
    for word, value in sorted_dict.items():
        output += f"{word} - {value}\n"
    return output




print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
