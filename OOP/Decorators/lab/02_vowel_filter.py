def vowel_filter(function):
    def wrapper():
        letters = function()
        return [l for l in letters if l.lower() in "aeiouy"]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e", "u", 'o', 'i']

print(get_letters())
