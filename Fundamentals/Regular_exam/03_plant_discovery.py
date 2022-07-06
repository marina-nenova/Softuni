class Plant:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.ratings = []

    def rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return 0


plants = {}

n = int(input())
for num in range(n):
    data = input().split('<->')
    plant_name = data[0]
    plant_rarity = int(data[1])
    plants[plant_name] = Plant(plant_name, plant_rarity)

command = input()

while not command == 'Exhibition':
    data_1 = command.split(': ')
    data_2 = data_1[1].split(' - ')
    plant_name = data_2[0]
    action = data_1[0]

    if plant_name not in plants:
        print('error')

    elif action == 'Rate':
        rating = int(data_2[1])
        plants[plant_name].ratings.append(rating)

    elif action == 'Update':
        new_rarity = int(data_2[1])
        plants[plant_name].rarity = new_rarity

    elif action == 'Reset':
        plants[plant_name].ratings.clear()

    command = input()

print(f'Plants for the exhibition:')

for plant in plants.values():
    print(f'- {plant.name}; Rarity: {plant.rarity}; Rating: {plant.rating():.2f}')