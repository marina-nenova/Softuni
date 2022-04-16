# import re
#
# demon_names = [name.strip() for name in input().split(",")]
#
# health_pattern = r"[^0-9+\-*\/\.]"
# damage_pattern = r"[+|-]?\d+\.?\d*"
# signs_pattern = r"[/*]"
#
# demon_info = {}
# for name in demon_names:
#
#     char_list = re.findall(health_pattern, name)
#     demon_health = sum(ord(char) for char in char_list)
#     num_matches = re.findall(damage_pattern, name)
#     signs_list = re.findall(signs_pattern, name)
#
#     demon_damage = 0
#     for num in num_matches:
#         demon_damage += float(num)
#
#     for sign in signs_list:
#         if sign == "*":
#             demon_damage *= 2
#         elif sign == "/":
#             demon_damage /= 2
#
#     demon_info[name] = [demon_health, demon_damage]
#
# for demon in sorted(demon_info):
#     print(f"{demon} - {demon_info[demon][0]} health, {demon_info[demon][1]:.2f} damage")

import re

data = sorted([x.strip() for x in input().split(',')])
for name in data:
    total_health = sum([ord(x) for x in re.findall(r'[^0-9+\-*/.]', name)])
    damage = sum([float(x.group()) for x in re.finditer(r'[+-]?\d(\.\d+)?', name)])
    multiply_divide = ([x for x in re.findall(r'[*/]', name)])
    for symbol in multiply_divide:
        if symbol == '*':
            damage *= 2
        else:
            damage /= 2
    print(f'{name} - {total_health} health, {damage:.2f} damage')