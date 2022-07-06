tournament_days = int(input())
total_money_won = 0
total_games_won = 0
total_games_lost = 0

for day in range(tournament_days):
    type_of_sport = input()
    money_won_per_day = 0
    games_won_per_day = 0
    games_lost_per_day = 0
    while type_of_sport != "Finish":
        result = input()
        if result == "win":
            money_won_per_day += 20
            games_won_per_day += 1
        elif result == "lose":
            games_lost_per_day += 1
        type_of_sport = input()
    total_games_won += games_won_per_day
    total_games_lost += games_lost_per_day

    if games_won_per_day > games_lost_per_day:
        money_won_per_day += money_won_per_day * 0.1
    total_money_won += money_won_per_day

if total_games_won > total_games_lost:
    total_money_won += total_money_won * 0.2
    print(f"You won the tournament! Total raised money: {total_money_won:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money_won:.2f}")
