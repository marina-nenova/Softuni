class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book title {self.title} from author {self.author} with pages {self.pages}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        try:
            return [book for book in self.books if book.title == title][0]
        except IndexError:
            return "Book not found"


library = Library()

for idx in range(1, 21):
    book = Book(f"Title{idx}", f"Author{idx}", 100 + idx)
    library.add_book(book)

print(library.find_book("Title1"))
