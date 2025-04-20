class Book:
    material = "paper"
    with_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def book_details(self):
        if self.reserved:
            print(
                f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Material: {self.material}, reserved"
            )
        else:
            print(
                f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Material: {self.material}"
            )


first_book = Book(
    "Reminiscences of a Stock Operator", "Edwin Lefevre", 384, 1234, reserved=False
)
second_book = Book(
    "World's Greatest Stock Trader", "Rich Smith", 289, 2345, reserved=True
)
third_book = Book("Market Wizards", "Schwagger", 301, 3456)
forth_book = Book("One Up on Wall Street", "Peter Lynch", 418, 4567)
fifth_book = Book("The Intelligent Investor", "Ben Graham", 624, 5678, reserved=True)

first_book.book_details()
second_book.book_details()
third_book.book_details()
forth_book.book_details()
fifth_book.book_details()
