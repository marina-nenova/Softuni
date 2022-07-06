name_of_team = input()
number_of_matches = int(input())
total_wins = 0
total_draws = 0
total_losses = 0
total_points = 0
no_matches_played = False
if number_of_matches == 0:
    no_matches_played = True
for match in range(number_of_matches):
    outcome = input()
    if outcome == "W":
        total_wins += 1
        total_points += 3
    elif outcome == "D":
        total_draws += 1
        total_points += 1
    elif outcome == "L":
        total_losses += 1
if no_matches_played:
    print(f"{name_of_team} hasn't played any games during this season.")
else:
    win_rate = (total_wins / number_of_matches) * 100
    print(f"{name_of_team} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {total_wins}")
    print(f"## D: {total_draws}")
    print(f"## L: {total_losses}")
    print(f"Win rate: {win_rate:.2f}%")