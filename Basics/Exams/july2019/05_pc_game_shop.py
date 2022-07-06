games_sold = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0
for game in range(games_sold):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1

hearthstone_sold = (hearthstone / games_sold) * 100
fornite_sold = (fornite / games_sold) * 100
overwatch_sold = (overwatch / games_sold) * 100
others_sold = (others / games_sold) * 100

print(f"Hearthstone - {hearthstone_sold:.2f}%")
print(f"Fornite - {fornite_sold:.2f}%")
print(f"Overwatch - {overwatch_sold:.2f}%")
print(f"Others - {others_sold:.2f}%")

