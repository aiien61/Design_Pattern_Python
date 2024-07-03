"""
You are given a class called Person. The person has two attributes: id, and name .

Implement a PersonFactory that has a non-static create_person() method that takes a person's name 
and return a person initialized with this name and an id.

The id of the person should be set as a 0-based index of the object created. So, the first person 
the factory makes should have Id = 0, second Id = 1 and so on.
"""


class Person:
    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name


class PersonFactory:
    Id: int = 0

    def create_person(self, name: str) -> Person:
        new_person = Person(self.Id, name)
        self.Id += 1
        return new_person
