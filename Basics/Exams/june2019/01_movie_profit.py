movie_name = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_per_ticket = float(input())
percentage_for_the_cinema = int(input())

income_per_day = number_of_tickets * price_per_ticket
total_income = income_per_day * number_of_days
cinema_deduction = total_income * (percentage_for_the_cinema / 100)
total_profit = total_income - cinema_deduction

print(f"The profit from the movie {movie_name} is {total_profit:.2f} lv.")