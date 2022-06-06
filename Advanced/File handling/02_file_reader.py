import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path, "custom_files", "numbers.txt")

try:
    with open(file_path) as file:
        sum_nums = sum([int(line) for line in file.readlines()])
        print(sum_nums)
except FileNotFoundError:
    print("File was not found.")
