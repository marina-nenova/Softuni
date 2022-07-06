command = input()
matches_won = 0
matches_lost = 0
total_games = 0
while command != "End of tournaments":
    name_of_tournament = command
    games_per_tournament = int(input())
    total_games += games_per_tournament
    for game in range(1, games_per_tournament + 1):
        desi_team_points = int(input())
        rival_team_points = int(input())
        difference = abs(desi_team_points - rival_team_points)
        if desi_team_points > rival_team_points:
            matches_won += 1
            print(f"Game {game} of tournament {name_of_tournament}: win with {difference} points.")
        if rival_team_points > desi_team_points:
            matches_lost += 1
            print(f"Game {game} of tournament {name_of_tournament}: lost with {difference} points.")
    command = input()

matches_won_percentage = (matches_won / total_games) * 100
matches_lost_percentage = (matches_lost / total_games) * 100

print(f"{matches_won_percentage:.2f}% matches win")
print(f"{matches_lost_percentage:.2f}% matches lost")