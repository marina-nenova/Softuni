#
# total = 0
#
# while True:
#     command = input()
#     if command == "NoMoreMoney":
#         break
#     elif float(command) < 0:
#         print("Invalid operation!")
#         break
#     print(f"Increase: {float(command):.2f}")
#     total += float(command)
#
# print(f"Total: {total:.2f}")

command = input()
total = 0

while command != "NoMoreMoney":
    sum = float(command)
    if sum < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {float(command):.2f}")
    total += sum
    command = input()
print(f"Total: {total:.2f}")