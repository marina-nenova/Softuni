from Classes_and_objects.exercise.guild_system.project.player import Player
from Classes_and_objects.exercise.guild_system.project.guild import Guild

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
