def concatenate(*args, **kwargs):
    output = ""
    for el in args:
        output += el

    for key, value in kwargs.items():
        if key in output:
            output = output.replace(key, value)
    return output




print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))