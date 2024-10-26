from .person import Person, Member, Librarian

class PersonFactory:
    def __init__(self, person_type: str = "person"):
        self.person_type = person_type

    def get_person(self, person_id: str, person_name: str, person_type: str = None):
        person_type = person_type or self.person_type
        if person_type == "person":
            return Person(person_name, person_id)
        elif person_type == "member":
            return Member(person_name, person_id)
        elif person_type == "librarian":
            return Librarian(person_name, person_id)
