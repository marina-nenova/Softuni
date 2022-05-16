# favourite_book = input()
# counter = 0
# while True:
#     checked_book = input()
#     if checked_book == "No More Books":
#         print("The book you search is not here!")
#         print(f"You checked {counter} books.")
#         break
#
#     if checked_book != favourite_book:
#         counter += 1
#
#     else:
#         print(f"You checked {counter} books and found it." )
#         break
#
# favourite_book = input()
# counter = 0
# checked_book = ""

# while checked_book != favourite_book:
#     checked_book = input()
#     if checked_book == "No More Books":
#         print("The book you search is not here!")
#         print(f"You checked {counter} books.")
#         break
#     if checked_book != favourite_book:
#         counter += 1
#
# if checked_book == favourite_book:
#     print(f"You checked {counter} books and found it."

favourite_book = input()
counter = 0
book_is_found = False
next_book = input()

while next_book != "No More Books":
    if next_book == favourite_book:
        book_is_found = True
        break
    counter += 1
    next_book = input()
if book_is_found:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")