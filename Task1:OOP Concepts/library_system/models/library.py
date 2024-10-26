from .book import Book

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book: Book):
        self.__books.append(book)
        print(f"Added \"{book.get_title()}\" by \"{book.get_author()}\" to the library collection.")

    def list_books(self):
        if not self.__books:
            print("No books available in the library.")
        for book in self.__books:
            print(book)
