from models.adapter import SpanishBookAdapter
from models.book import Book, SpanishBook
from models.library import Library
from models.person import Member, Librarian
from models.factory import PersonFactory

# Set up library and books
library = Library()
book1 = Book("A Great Book By a Great Writer", "A Great Writer", "123456789")
book2 = Book("Not a Great Book", "Not A Great Writer", "987654321")
library.add_book(book1)
library.add_book(book2)

# Create members and librarians
member1 = Member("Tanim", "1")
member2 = Member("Shan", "2")
librarian = Librarian("Tanzil", "10")

# Access library and manage books
print(member1.access_library())
print(librarian.issue_book(book1, member1))

# Use factory
print("\nUsing factory", '='*20, ">")
person_factory = PersonFactory("member")
member3 = person_factory.get_person("3", "Tom")
librarian2 = person_factory.get_person("11", "Tiger", "librarian")

# Adapting Spanish book
spanish_book = SpanishBook("El Gran Libro", "Un Gran Escritor", "987321654")
adapted_book = SpanishBookAdapter(spanish_book)

library.add_book(adapted_book)
print("\n", member3.access_library())
print(librarian2.issue_book(adapted_book, member3))