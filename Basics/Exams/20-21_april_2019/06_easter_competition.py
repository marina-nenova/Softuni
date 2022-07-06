number_easter_breads = int(input())
highest_score = 0
winner = ""
for easter_bread in range(number_easter_breads):
    baker_name = input()
    command = input()
    baker_score = 0
    while command != "Stop":
        score = int(command)
        baker_score += score
        command = input()
    print(f"{baker_name} has {baker_score} points.")
    if baker_score > highest_score:
        highest_score = baker_score
        winner = baker_name
        print(f"{baker_name} is the new number 1!")
print(f"{winner} won competition with {highest_score} points!")