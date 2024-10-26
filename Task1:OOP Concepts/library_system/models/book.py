class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_details(self):
        return f"Title: {self.get_title()}, Writer: {self.get_author()}, Code: {self.get_isbn()}"


class SpanishBook:
    def __init__(self, título: str, autor: str, unique_code: str):
        self.título = título
        self.autor = autor
        self.unique_code = unique_code

    def get_details(self):
        return f"Title: {self.título}, Writer: {self.autor}, Code: {self.unique_code}"
