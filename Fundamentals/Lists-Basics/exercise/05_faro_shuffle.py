cards = input().split()
number_of_shuffles = int(input())
middle = int((len(cards) / 2))

for shuffle in range(number_of_shuffles):
    current_shuffle = []
    first_half = cards[0:middle]
    second_half = cards[middle::]
    for index in range(len(first_half)):
        current_shuffle.append(first_half[index])
        current_shuffle.append(second_half[index])
    cards = current_shuffle

print(cards)
