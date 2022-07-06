# •	Предпазен найлон - 1.50 лв. за кв. метър
# •	Боя - 14.50 лв. за литър
# •	Разредител за боя - 5.00 лв. за литър

nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours = int(input())

nylon_sum = (nylon_needed + 2) * 1.5
paint_sum = (paint_needed + (paint_needed * 0.1)) * 14.5
thinner_sum = thinner_needed * 5

materials_expenses = nylon_sum + paint_sum + thinner_sum + 0.4
workers_expenses_per_hour = materials_expenses * 0.3
workers_expenses = workers_expenses_per_hour * hours
final_sum = materials_expenses + workers_expenses
print(final_sum)
