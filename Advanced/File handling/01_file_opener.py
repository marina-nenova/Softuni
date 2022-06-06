import os
#file is in currents dir
# try:
#     file = open("example.txt", "r")
#     print("File found")
# except FileNotFoundError:
#     print("File not found")

#file is one folder inner
absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path, "custom_files", "something.txt")
file = open(file_path)
print(file.readlines())
file.close()

#file is one folder back
# file_path = os.path.abspath("../example.txt")
# print(file_path)
# file = open(file_path)
# print(file.readlines())