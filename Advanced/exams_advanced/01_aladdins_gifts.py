from collections import deque

materials = [int(el) for el in input().split()]
magic = deque([int(el) for el in input().split()])
crafted_presents = {}

while magic and materials:
    current_material = materials.pop()
    current_magic = magic.popleft()

    sum = current_material + current_magic

    if sum < 100:
        if sum % 2 == 0:
            sum = (current_material * 2) + (current_magic * 3)
        elif sum % 2 != 0:
            sum *= 2
    if sum > 499:
        sum /= 2

    if 100 <= sum < 200:
        present = "Gemstone"
    elif 200 <= sum < 300:
        present = "Porcelain Sculpture"
    elif 300 <= sum < 400:
        present = "Gold"
    elif 400 <= sum < 500:
        present = "Diamond Jewellery"
    else:
        continue

    if present not in crafted_presents:
        crafted_presents[present] = 0
    crafted_presents[present] += 1

if ("Gemstone" in crafted_presents and "Porcelain Sculpture" in crafted_presents) or \
        ("Gold" in crafted_presents and "Diamond Jewellery") in crafted_presents:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(el) for el in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(el) for el in magic])}")

for present, count in sorted(crafted_presents.items()):
    print(f"{present}: {count}")


# from collections import deque
#
# materials = [int(el) for el in input().split()]
# magic = deque([int(el) for el in input().split()])
#
# gifts = {"Gemstone": range(100, 200), "Porcelain Sculpture": range(200, 300), "Gold": range(300, 400), "Diamond Jewellery": range(400, 500)}
# gifts_made = {}
#
# while magic and materials:
#     current_material = materials.pop()
#     current_magic = magic.popleft()
#
#     current_sum = current_magic + current_material
#
#     if current_sum < 100:
#         if current_sum % 2 == 0:
#             current_sum = current_material * 2 + current_magic * 3
#         else:
#             current_sum *= 2
#
#     elif current_sum >= 500:
#         current_sum //= 2
#
#     for gift, range in gifts.items():
#         if current_sum in range:
#             current_gift = gift
#             if current_gift not in gifts_made:
#                 gifts_made[current_gift] = 0
#             gifts_made[current_gift] += 1
#             break
#
# if ("Gemstone" in gifts_made and "Porcelain Sculpture" in gifts_made) or ("Gold" in gifts_made and "Diamond Jewellery" in gifts_made):
#     print("The wedding presents are made!")
# else:
#     print("Aladdin does not have enough wedding presents.")
#
# if materials:
#     print(f"Materials left: {', '.join([str(el) for el in materials])}")
#
# if magic:
#     print(f"Magic left: {', '.join([str(el) for el in magic])}")
#
# for gift, amount in sorted(gifts_made.items()):
#     print(f"{gift}: {amount}")
