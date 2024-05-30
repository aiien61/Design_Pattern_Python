"""Dependency Inversion Principle 依賴反轉原則: 
1. high-level modules should not depend on low-level modules.
2. use abstractions.
"""

from abc import abstractmethod
from enum import Enum, auto

class Relationship(Enum):
    PARENT = auto()
    CHILD = auto()
    SIBLING = auto()

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


# low-level
class Relationships(RelationshipBrowser):
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research:
    # dependency on a low-level module directly
    # bad because strongly dependent on e.g. storage type
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, relationships: Relationships):
        # high-level: find all of john's children
        for p in relationships.find_all_children_of('John'):
            print(f'John has a child called {p}.')


class Notification:
    def send(self, message: str): pass

class EmailNotification(Notification):
    def send(self, message: str):
        print(f'Send Email Notification: {message}')

class SMSNotification(Notification):
    def send(self, message: str):
        print(f'Send Text Notification: {message}')

class UserManager:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send_notification(self, user, message: str):
        self.notification.send(f'{user}: {message}')


if __name__ == '__main__':
    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships)

    email_notification = EmailNotification()
    sms_notification = SMSNotification()
    user_manager = UserManager(email_notification)
    user_manager.send_notification('John', 'Welcome to our website!')

    user_manager = UserManager(sms_notification)
    user_manager.send_notification('Bob', 'The order you placed is on the way!')