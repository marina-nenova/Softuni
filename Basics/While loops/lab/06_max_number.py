# import sys
#
# max_number = -sys.maxsize
#
# while True:
#     command = input()
#     if command == "Stop":
#         break
#     elif int(command) > max_number:
#         max_number = int(command)
# print(max_number)
import sys

max_number = -sys.maxsize
command = input()

while command != "Stop":
    number = int(command)
    if number > max_number:
        max_number = number
    command = input()
print(max_number)