num_of_pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

hours_per_book = int(num_of_pages / pages_per_hour)
hours_needed = hours_per_book / days_per_book
print(int(hours_needed))