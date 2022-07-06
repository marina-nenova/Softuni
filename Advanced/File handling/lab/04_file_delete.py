import os

file_path = "my_first_file.txt"
try:
    os.remove("my_first_file.txt")
except FileNotFoundError:
    print('File already deleted!')