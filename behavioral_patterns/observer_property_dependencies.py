from abc import ABC, abstractmethod
from typing import Any, List


class Event(list):
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self) -> None:
        self.property_changed: Event = Event()


class Person(PropertyObservable):
    def __init__(self, age: int=0) -> None:
        super().__init__()
        self._age: int = age

    @property
    def can_vote(self) -> bool:
        return self._age >= 20

    @property
    def age(self): return self._age

    @age.setter
    def age(self, value: int):
        old_can_vote: bool = self.can_vote
        if self._age != value:    
            self._age = value
            self.property_changed('age', value)

        if old_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)


if __name__ == '__main__':
    def person_changed(name: str, value: int):
        if name == 'can_vote':
            print(f'Votting ability changed to {value}')

    p = Person()
    p.property_changed.append(person_changed)

    for age in range(16, 25):
        print(f'Changing age to {age}')
        p.age = age
