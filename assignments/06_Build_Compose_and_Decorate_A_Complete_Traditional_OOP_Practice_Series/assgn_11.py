# Class Methods
"""
Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.
"""

class Book:
    # Class variable to keep track of total books
    total_books = 0

    def __init__(self, title):
        self.title = title
        # Call the class method to increment book count whenever a new book is created
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

book = Book("HOLY QURAN")
book = Book("BUKHARI SHARIF")
print(Book.total_books)
