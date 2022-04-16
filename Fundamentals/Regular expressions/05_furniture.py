import re

pattern = r"^>>(?P<name>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)$"
command = input()
total_sum = 0
print("Bought furniture:")
while command != "Purchase":
    match = re.search(pattern, command)
    if match is not None:
        print(match.group("name"))
        total_sum += float(match.group("price")) * int(match.group("quantity"))
    command = input()

print(f"Total money spend: {total_sum:.2f}")

# import re
# command = input()
# furniture_bought = {}
# pattern = r">>(?P<furniture>\w+)<<(?P<price>\d+\.?(\d+)?)!(?P<quantity>\d+)"
# while not command == "Purchase":
#     valid_purchase = re.match(pattern, command)
#     if valid_purchase and valid_purchase.group('furniture' and 'price' and 'quantity'):
#         sum_of_purchase = float(valid_purchase.group('price')) * int(valid_purchase.group('quantity'))
#         if sum_of_purchase > 0:
#             furniture_bought.setdefault(valid_purchase.group('furniture'), 0)
#             furniture_bought[valid_purchase.group('furniture')] += sum_of_purchase
#     command = input()
# print(f"Bought furniture:", *furniture_bought.keys(), sep="\n")
# print(f'Total money spend: {sum(furniture_bought.values()):.2f}')

# >>Sofa<<312.23!3
# >>TV<<300!5
# >>Sofa<<200!5
# Purchase