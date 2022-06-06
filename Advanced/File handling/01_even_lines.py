symbols_to_replace = ["-", ",", ".", "!", "?"]

with open("text.txt", "r") as file:
    text = file.readlines()
    for index in range(0, len(text), 2):
        line = text[index]
        reversed_line = ' '.join(reversed(line.split()))
        for symbol in symbols_to_replace:
            reversed_line = reversed_line.replace(symbol, "@")
        print(reversed_line)
