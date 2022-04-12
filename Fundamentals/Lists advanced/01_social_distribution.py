# population = [int(num) for num in input().split(", ")]
# minimum_wealth = int(input())
#
# for index in range(len(population)):
#     if population[index] < minimum_wealth:
#         needed = minimum_wealth - population[index]
#         wealthiest = max(population)
#         if wealthiest - needed >= minimum_wealth:
#             population[population.index(wealthiest)] -= needed
#             population[index] += needed
# if sum(population) >= len(population) * minimum_wealth:
#     print(population)
# else:
#     print("No equal distribution possible")

population_input = input().split(", ")
population = list(map(int, population_input))
wealth = int(input())
distributed_list = []

for i in population:

    if i < wealth:
        diff = abs(wealth - i)
        wealthiest = max(population)
        wealthiest_index = population.index(wealthiest)
        if wealthiest - diff >= wealth:
            wealthiest -= diff
            i += diff
        distributed_list.append(i)
        population[wealthiest_index] = wealthiest
    else:
        distributed_list.append(i)

if sum(distributed_list) >= len(distributed_list) * wealth:
    print(distributed_list)
else:
    print("No equal distribution possible")
