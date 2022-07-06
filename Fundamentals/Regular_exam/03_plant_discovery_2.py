n = int(input())

plants_info = {}
for _ in range(n):
    name, rarity = input().split('<->')
    plants_info[name] = {'rarity': rarity, 'rating': []}

command = input()

while not command == "Exhibition":
    data = command.split(": ")
    data_1 = data[1].split(" - ")
    action = data[0]
    plant = data_1[0]
    if plant not in plants_info:
        print("error")
    elif action == "Rate":
        rating = int(data_1[1])
        plants_info[plant]['rating'].append(rating)
    elif action == "Update":
        new_rarity = data_1[1]
        plants_info[plant]['rarity'] = new_rarity
    elif action == "Reset":
        plants_info[plant]['rating'].clear()
    command = input()

print("Plants for the exhibition:")

for plant, info in plants_info.items():
    average_rating = 0
    if info['rating']:
        average_rating = sum(info['rating']) / len(info['rating'])
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {average_rating:.2f}")

