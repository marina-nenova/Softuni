# import sys
#
# min_number = sys.maxsize
#
# while True:
#     command = input()
#     if command == "Stop":
#         break
#     elif int(command) < min_number:
#         min_number = int(command)
# print(min_number)

import sys

min_number = sys.maxsize
command = input()

while command != "Stop":
    number = int(command)
    if number < min_number:
        min_number = number
    command = input()
print(min_number)