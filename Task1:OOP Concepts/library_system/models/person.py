class Person:
    def __init__(self, name: str, person_id: str):
        self.__name = name
        self.__person_id = person_id

    def get_name(self):
        return self.__name

    def get_person_id(self):
        return self.__person_id


class Member(Person):
    def __init__(self, name: str, person_id: str):
        super().__init__(name, person_id)

    def access_library(self):
        return f"Member \"{self.get_name()}\" with ID \"{self.get_person_id()}\" is accessing the library."


class Librarian(Person):
    def __init__(self, name: str, person_id: str):
        super().__init__(name, person_id)

    def issue_book(self, book, member):
        return f"Librarian \"{self.get_name()}\" issued \"{book.get_title()}\" to member \"{member.get_name()}\"."

    def return_book(self, book, member):
        return f"Librarian \"{self.get_name()}\" received \"{book.get_title()}\" back from member \"{member.get_name()}\"."
