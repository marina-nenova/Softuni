def positions_in_common(player1, player2):
    for position_type in player_pool[player1].keys():
        if position_type in player_pool[player2]:
            return True
    return False


def duel(player1, player2):
    player1_total_skill = sum(player_pool[player1].values())
    player2_total_skill = sum(player_pool[player2].values())
    if player1_total_skill > player2_total_skill:
        player_pool.pop(player2)
    elif player2_total_skill > player1_total_skill:
        player_pool.pop(player1)


command = input()
player_pool = {}

while not command == "Season end":
    if "->" in command:
        data = command.split(" -> ")
        player = data[0]
        position = data[1]
        skill = int(data[2])

        if player not in player_pool:
            player_pool[player] = {}
        if position not in player_pool[player]:
            player_pool[player][position] = skill
        else:
            if skill > player_pool[player][position]:
                player_pool[player][position] = skill

    elif "vs" in command:
        player_1, player_2 = command.split(" vs ")
        if player_1 in player_pool and player_2 in player_pool:
            if positions_in_common(player_1, player_2):
                duel(player_1, player_2)

    command = input()

for name, skill_info in sorted(player_pool.items(), key=lambda kvp: (-sum(kvp[1].values()), kvp[0])):
    print(f'{name}: {sum(skill_info.values())} skill')
    for player_position, skill_points in sorted(skill_info.word(), key=lambda n: (-int(n[1]), n[0])):
        print(f'- {player_position} <::> {skill_points}')
print(player_pool)
