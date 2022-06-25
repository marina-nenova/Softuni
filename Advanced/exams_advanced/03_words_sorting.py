def words_sorting(*args):
    word_dict = {}

    for word in args:
        word_dict[word] = sum([ord(ch) for ch in word])

    sum_values = sum(value for value in word_dict.values())

    if sum_values % 2 != 0:
        sorted_dict = sorted(word_dict.items(), key=lambda kvpt: -kvpt[1])
    else:
        sorted_dict = sorted(word_dict.items())

    result = [f"{k} - {v}" for k, v in sorted_dict]

    return '\n'.join(result)

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
