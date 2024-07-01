from abc import ABC, abstractmethod
from typing import Any, List

class Event(list):
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)

def call_doctor(name: str, address: str) -> None:
    print(f'{name} needs a doctor at {address}')

if __name__ == '__main__':
    person = Person('Sherlock', '221B Baker St.')
    person.falls_ill.append(lambda name, address: print(f'{name} is ill.'))
    person.falls_ill.append(call_doctor)

    person.catch_a_cold()

    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()
