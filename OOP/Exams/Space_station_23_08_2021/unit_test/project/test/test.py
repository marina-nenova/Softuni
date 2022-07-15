from project.library import Library
from unittest import TestCase, main


class LibraryTests(TestCase):
    def setUp(self) -> None:
        self.library = Library("Test")
        self.library.books_by_authors = {"A": ["book 1", "book 2"]}
        self.library.readers = {"John": []}

    def test_library_initialized_correctly_with_valid_data(self):
        name = "Test"
        library = Library(name)
        self.assertEqual(name, library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_name_initialized_with_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            Library("")
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_if_author_not_in_books_by_authors(self):
        self.library.add_book("B", "book 3")
        self.assertEqual({"A": ["book 1", "book 2"], "B": ["book 3"]}, self.library.books_by_authors)

    def test_add_book_if_author_exists(self):
        self.library.add_book("A", "book 3")
        self.assertEqual({"A": ["book 1", "book 2", "book 3"]}, self.library.books_by_authors)
        self.library.add_book("A", "book 4")
        self.assertEqual({"A": ["book 1", "book 2", "book 3", "book 4"]}, self.library.books_by_authors)

    def test_add_book_if_book_exists(self):
        self.library.add_book("A", "book 2")
        self.assertEqual({"A": ["book 1", "book 2"]}, self.library.books_by_authors)

    def test_add_reader_that_does_not_exist(self):
        self.library.add_reader("Peter")
        self.assertEqual({"John": [], "Peter": []}, self.library.readers)

    def test_add_reader_if_reader_exists_returns_correctly(self):
        result = self.library.add_reader("John")
        self.assertEqual("John is already registered in the Test library.", result)

    def test_rent_book_if_reader_doesnt_exist(self):
        result = self.library.rent_book("Peter", "A", "book 1")
        expected = "Peter is not registered in the Test Library."
        self.assertEqual(expected, result)

    def test_rent_book_if_author_not_in_library(self):
        result = self.library.rent_book("John", "B", "book 3")
        expected = "Test Library does not have any B's books."
        self.assertEqual(expected, result)

    def test_rent_book_if_book_title_not_in_library(self):
        result = self.library.rent_book("John", "A", "book 3")
        expected = """Test Library does not have A's "book 3"."""
        self.assertEqual(expected, result)

    def test_rent_book_adds_book_to_readers_list(self):
        self.library.rent_book("John", "A", "book 2")
        self.assertEqual({"John": [{"A": "book 2"}]}, self.library.readers)

        self.library.rent_book("John", "A", "book 1")
        self.assertEqual({"John": [{"A": "book 2"}, {"A": "book 1"}]}, self.library.readers)

    def test_rent_book_removes_title_from_authors_books_list(self):
        self.library.rent_book("John", "A", "book 2")
        self.assertEqual({"A": ["book 1"]}, self.library.books_by_authors)

        self.library.rent_book("John", "A", "book 1")
        self.assertEqual({"A": []}, self.library.books_by_authors)


if __name__ == "__main__":
    main()
