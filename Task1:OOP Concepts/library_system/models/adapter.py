from library_system.models.book import Book, SpanishBook


class SpanishBookAdapter(Book):
    def __init__(self, spanish_book: SpanishBook):
        super().__init__(title=spanish_book.título, author=spanish_book.autor, isbn=spanish_book.unique_code)
        self.spanish_book = spanish_book

    def __str__(self):
        return f"ExternalBookAdapter: {self.spanish_book.get_details()}"
