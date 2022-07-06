import re

with open("text.txt", "r") as file, open("output.txt", "w") as output_file:
    for row, line in enumerate(file):
        stripped_line = line.strip()
        letters_count = len(re.findall("[A-Za-z]", stripped_line))
        signs_count = len(re.findall("[^A-Za-z\s\d]", stripped_line))
        output_file.write(f"Line {row + 1}: {stripped_line} ({letters_count})({signs_count})\n")
