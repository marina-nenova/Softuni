def plunder(city, people, gold):
    targets[city]['population'] -= people
    targets[city]['gold'] -= gold
    print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
    if targets[city]['population'] == 0 or targets[city]['gold'] == 0:
        del targets[city]
        print(f"{city} has been wiped off the map!")


def prosper(city, gold_added):
    if gold_added < 0:
        print("Gold added cannot be a negative number!")
    else:
        targets[city]['gold'] += gold_added
        print(f"{gold_added} gold added to the city treasury. {city} now has {targets[city]['gold']} gold.")


command_1 = input()

targets = {}
while not command_1 == "Sail":
    city, population, gold = command_1.split("||")
    if city not in targets:
        targets[city] = {'population': 0, 'gold': 0}
    targets[city]['population'] += int(population)
    targets[city]['gold'] += int(gold)
    command_1 = input()

command_2 = input()

while not command_2 == "End":
    data = command_2.split("=>")
    action = data[0]
    city = data[1]
    if action == "Plunder":
        people= int(data[2])
        gold = int(data[3])
        plunder(city, people, gold)
    elif action == "Prosper":
        gold = int(data[2])
        prosper(city, gold)

    command_2 = input()

if targets:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    for town, info in targets.items():
        print(f"{town} -> Population: {info['population']} citizens, Gold: {info['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")