offers = input()
beggars = int(input())

offers_list = offers.split(", ")
offers_per_beggar = []
start_index = 0
for beggar in range(beggars):
    current_sum = 0
    for index in range(start_index, len(offers_list), beggars):
        current_sum += int(offers_list[index])
    offers_per_beggar.append(current_sum)
    start_index += 1
print(offers_per_beggar)
