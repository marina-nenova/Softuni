class Book:
    def __init__(self, title, author, content: str):
        self.title = title
        self.author = author
        self.content = content


class Formatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content


class PrePrintFlyer:
    @staticmethod
    def format(book):
        return f"-------\n{book.title}\n-------\n{book.author}\n-------"


class Printer:
    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)


normal_formatter = Formatter()
flier_formatter = PrePrintFlyer()

b = Book("Title 1", "Author 1", "Some content")
p = Printer(normal_formatter)
p2 = Printer(flier_formatter)
print(p.get_book(b))
print()
print()
print(p2.get_book(b))
