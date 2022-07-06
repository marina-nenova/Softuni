import sys

number_of_movies = int(input())
highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
all_movies_ratings = 0
movie_with_lowest_rating = ''
movie_with_highes_rating = ''
for movie in range(number_of_movies):
    name_of_movie = input()
    movie_ratings = float(input())
    all_movies_ratings += movie_ratings
    if movie_ratings < lowest_rating:
        lowest_rating = movie_ratings
        movie_with_lowest_rating = name_of_movie
    if movie_ratings > highest_rating:
        highest_rating = movie_ratings
        movie_with_highes_rating = name_of_movie
average_ratings = all_movies_ratings / number_of_movies
print(f"{movie_with_highes_rating} is with highest rating: {highest_rating:.1f}")
print(f"{movie_with_lowest_rating} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_ratings:.1f}")