cards = input().split()
a_team_cards = []
b_team_cards = []
game_terminated = False
for index in range(len(cards)):
    if "A" in cards[index]:
        if cards[index] in a_team_cards:
            continue
        a_team_cards.append(cards[index])
    if "B" in cards[index]:
        if cards[index] in b_team_cards:
            continue
        b_team_cards.append(cards[index])
    if len(a_team_cards) == 5 or len(b_team_cards) == 5:
        game_terminated = True
        break

team_a_players_count = 11 - len(a_team_cards)
team_b_players_count = 11 - len(b_team_cards)

print(f"Team A - {team_a_players_count}; Team B - {team_b_players_count}")

if game_terminated:
    print("Game was terminated")
