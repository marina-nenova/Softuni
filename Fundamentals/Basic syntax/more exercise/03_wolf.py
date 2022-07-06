animals = input()

animals_list = animals.split(", ")

animals_list.reverse()
wolf_position = animals_list.index("wolf")
if animals_list[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!" )