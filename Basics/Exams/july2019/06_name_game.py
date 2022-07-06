command = input()
most_points = 0
winner = ""
while command != "Stop":
    name_of_player = command
    points = 0
    for letter in name_of_player:
        number = int(input())
        if number == ord(letter):
            points += 10
        else:
            points += 2
    if points >= most_points:
        most_points = points
        winner = name_of_player
    command = input()

print(f"The winner is {winner} with {most_points} points!")