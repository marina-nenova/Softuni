from project.movie import Movie
from unittest import TestCase, main


class MovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Top Gun", 2022, 8.6)
        self.movie2 = Movie("The Avengers", 2012, 8)
        self.movie3 = Movie("The Godfather", 1972, 9.2)

    def test_movie_initialized_correctly_with_valid_data(self):
        name = "Top Gun"
        year = 2022
        rating = 9.2
        movie = Movie(name, year, rating)
        self.assertEqual(name, movie.name)
        self.assertEqual(year, movie.year)
        self.assertEqual(rating, movie.rating)
        self.assertEqual([], movie.actors)

    def test_movie_raises_if_name_is_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            Movie("", 2022, 8.6)
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_movie_raises_if_year_less_than_1887(self):
        with self.assertRaises(ValueError) as ex:
            Movie("Top Gun", 1886, 8.6)
        self.assertEqual("Year is not valid!", str(ex.exception))
        movie = Movie("Top Gun", 1887, 8.6)
        self.assertEqual(1887, movie.year)

    def test_add_actor_if_name_not_in_list(self):
        self.movie.add_actor("Tom Cruise")
        self.assertEqual(["Tom Cruise"], self.movie.actors)
        self.movie.add_actor("Miles Teller")
        self.assertEqual(["Tom Cruise", "Miles Teller"], self.movie.actors)

    def test_add_actor_if_name_exists_returns_correct_string(self):
        self.movie.add_actor("Tom Cruise")
        self.assertEqual(["Tom Cruise"], self.movie.actors)
        result = self.movie.add_actor("Tom Cruise")
        self.assertEqual(["Tom Cruise"], self.movie.actors)
        self.assertEqual("Tom Cruise is already added in the list of actors!", result)

    def test_greater_than_returns_correctly_when_comparing_ratings(self):
        result = self.movie > self.movie2
        self.assertEqual(f'"{self.movie.name}" is better than "{self.movie2.name}"', result)
        result = self.movie > self.movie3
        self.assertEqual(f'"{self.movie3.name}" is better than "{self.movie.name}"', result)
        self.movie3.rating = 8.6
        self.assertEqual(f'"{self.movie3.name}" is better than "{self.movie.name}"', result)

    def test_repr_method_returns_correct_string(self):
        self.movie.add_actor("Tom Cruise")
        self.movie.add_actor("Miles Teller")
        self.assertEqual(["Tom Cruise", "Miles Teller"], self.movie.actors)
        result = str(self.movie)
        expected = f"Name: Top Gun\n" \
                   f"Year of Release: 2022\n" \
                   f"Rating: 8.60\n" \
                   f"Cast: Tom Cruise, Miles Teller"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
