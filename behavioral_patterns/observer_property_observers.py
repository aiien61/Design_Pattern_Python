from abc import ABC, abstractmethod
from typing import Any, List


class Event(list):
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self) -> None:
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age: int=0) -> None:
        super().__init__()
        self._age = age
    
    @property
    def age(self): return self._age

    @age.setter
    def age(self, value: int):
        if self._age != value:
            self._age = value
            self.property_changed('age', value)


class TrafficAuthority:
    def __init__(self, person: Person):
        self.person = person
        person.property_changed.append(self.person_changed)

    def person_changed(self, name: str, value: int):
        if name == 'age':
            if value < 16:
                print('Sorry, you still cannot drive.')
            else: 
                print('Okay, you can drive now.')
                self.person.property_changed.remove(self.person_changed)


if __name__ == '__main__':
    p = Person()
    ta = TrafficAuthority(p)
    for age in range(14, 20):
        print(f'Setting age to {age}')
        p.age = age
