actors_budget = float(input())
command = input()

not_enough_money = False
while command != "ACTION":
    actor_name = command
    if len(actor_name) <= 15:
        actor_salary = float(input())
    else:
        actor_salary = 0.2 * actors_budget
    actors_budget -= actor_salary
    if actors_budget <= 0:
        not_enough_money = True
        break
    command = input()

if not_enough_money:
    print(f"We need {abs(actors_budget):.2f} leva for our actors.")
else:
    print(f"We are left with {actors_budget:.2f} leva.")