import sys

command = input()
number_of_movies = 0
best_movie = ""
best_score = - sys.maxsize
limit_reached = False
while command != "STOP":
    movie_name = command
    number_of_movies += 1
    letter_value = 0
    movie_score = 0
    for letter in movie_name:
        if "a" <= letter <= "z":
            letter_value = ord(letter) - (2 * len(movie_name))
        elif "A" <= letter <= "Z":
            letter_value = ord(letter) - len(movie_name)
        else:
            letter_value = ord(letter)
        movie_score += letter_value
    if movie_score > best_score:
        best_score = movie_score
        best_movie = movie_name
    if number_of_movies == 7:
        limit_reached = True
        break
    command = input()

if limit_reached:
    print("The limit is reached.")
print(f"The best movie for you is {best_movie} with {best_score} ASCII sum.")