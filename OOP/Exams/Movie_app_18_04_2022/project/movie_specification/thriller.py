from project.movie_specification.movie import Movie


class Thriller(Movie):
    MIN_AGE = 16

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = MIN_AGE):
        super().__init__(title, year, owner, age_restriction)
