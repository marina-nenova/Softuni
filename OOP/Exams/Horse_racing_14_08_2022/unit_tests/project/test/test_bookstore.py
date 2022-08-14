from unit_tests.project.bookstore import Bookstore
from unittest import TestCase, main


class BookstoreTests(TestCase):
    def test_bookstore_created_correctly_with_valid_data(self):
        bookstore = Bookstore(2)

        self.assertEqual(2, bookstore.books_limit)
        self.assertEqual({}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, bookstore.total_sold_books)
        self.assertEqual(0, bookstore._Bookstore__total_sold_books)

    def test_book_limit_zero_raises(self):
        with self.assertRaises(ValueError) as ve:
            Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_book_limit_negative_raises(self):
        with self.assertRaises(ValueError) as ve:
            Bookstore(-1)
        self.assertEqual(f"Books limit of -1 is not valid", str(ve.exception))

    def test_len_method_returns_correct_number(self):
        bookstore = Bookstore(3)
        result = len(bookstore)
        self.assertEqual(0, result)

        bookstore.receive_book("LOTR", 1)
        bookstore.receive_book("Witcher", 2)

        result = len(bookstore)
        self.assertEqual(3, result)

    def test_receive_book_if_not_enough_space_raises(self):
        bookstore = Bookstore(3)
        bookstore.receive_book("LOTR", 1)
        bookstore.receive_book("Witcher", 2)
        with self.assertRaises(Exception) as ex:
            bookstore.receive_book("Harry Potter", 1)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_if_book_title_doesnt_exist(self):
        bookstore = Bookstore(3)
        bookstore.receive_book("LOTR", 1)
        bookstore.receive_book("Witcher", 1)
        self.assertEqual(2, len(bookstore))

        result = bookstore.receive_book("Harry Potter", 0)
        self.assertEqual({"LOTR": 1, "Witcher": 1, "Harry Potter": 0}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual("0 copies of Harry Potter are available in the bookstore.", result)

        result = bookstore.receive_book("Hobbit", 1)
        self.assertEqual({"LOTR": 1, "Witcher": 1, "Harry Potter": 0, "Hobbit": 1}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual("1 copies of Hobbit are available in the bookstore.", result)

    def test_receive_book_if_book_title_exists(self):
        bookstore = Bookstore(3)
        bookstore.receive_book("LOTR", 1)
        self.assertEqual(1, len(bookstore))
        result = bookstore.receive_book("LOTR", 2)
        self.assertEqual({"LOTR": 3}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual("3 copies of LOTR are available in the bookstore.", result)

    def test_sell_book_if_book_doesnt_exist_raises(self):
        bookstore = Bookstore(3)
        self.assertEqual({}, bookstore.availability_in_store_by_book_titles)
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("Harry Potter", 1)
        self.assertEqual("Book Harry Potter doesn't exist!", str(ex.exception))

    def test_sell_book_if_not_enough_copies_raises(self):
        bookstore = Bookstore(3)
        bookstore.receive_book("LOTR", 1)
        bookstore.receive_book("Witcher", 1)
        self.assertEqual({"LOTR": 1, "Witcher": 1}, bookstore.availability_in_store_by_book_titles)
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book("LOTR", 2)
        self.assertEqual("LOTR has not enough copies to sell. Left: 1", str(ex.exception))
        self.assertEqual({"LOTR": 1, "Witcher": 1}, bookstore.availability_in_store_by_book_titles)

    def test_sell_book_if_enough_copies(self):
        bookstore = Bookstore(3)
        bookstore.receive_book("LOTR", 2)
        bookstore.receive_book("Witcher", 1)
        result = bookstore.sell_book("LOTR", 2)
        self.assertEqual({"LOTR": 0, "Witcher": 1}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(f"Sold 2 copies of LOTR", result)
        self.assertEqual(2, bookstore.total_sold_books)
        self.assertEqual(2, bookstore._Bookstore__total_sold_books)

    def test_string_method_returns_correctly(self):
        bookstore = Bookstore(3)
        bookstore.receive_book("LOTR", 2)
        bookstore.receive_book("Witcher", 1)
        bookstore.sell_book("LOTR", 1)
        result = str(bookstore)
        expected = "Total sold books: 1\nCurrent availability: 2\n - LOTR: 1 copies\n - Witcher: 1 copies"
        self.assertEqual(expected, result)

    def test_string_method_if_not_books(self):
        bookstore = Bookstore(3)
        result = str(bookstore)
        expected = "Total sold books: 0\nCurrent availability: 0"
        self.assertEqual(expected, result)

    def test_total_sold_books_returns_correct_number(self):
        bookstore = Bookstore(4)
        bookstore.receive_book("LOTR", 3)
        bookstore.receive_book("Witcher", 1)

        result = bookstore.sell_book("LOTR", 2)
        self.assertEqual({"LOTR": 1, "Witcher": 1}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(f"Sold 2 copies of LOTR", result)
        self.assertEqual(2, bookstore.total_sold_books)
        self.assertEqual(2, bookstore._Bookstore__total_sold_books)

        result = bookstore.sell_book("LOTR", 1)
        self.assertEqual({"LOTR": 0, "Witcher": 1}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(f"Sold 1 copies of LOTR", result)
        self.assertEqual(3, bookstore.total_sold_books)
        self.assertEqual(3, bookstore._Bookstore__total_sold_books)


if __name__ == "__main__":
    main()