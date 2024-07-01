from abc import ABC, abstractmethod
from typing import List

class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings: List[str]

    def prepare(self):
        print(f"Prepare {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print(f"Adding toppings: {', '.join(self.toppings)}")

    def bake(self):
        print("Bake for 25 minutes at 350")
    
    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def get_name(self):
        return self.name
    
    def to_string(self):
        display: StringBuffer = StringBuffer()
        display.append(f"----- {self.name} -----\n")
        display.append(f"{self.dough}\n")
        display.append(f"{self.sauce}\n")
        for topping in self._toppings:
            display.append(f"{topping}\n")
        return display.to_string()
    
class StringBuffer:
    def __init__(self):
        self.lst: List[str] = []

    def append(self, string: str) -> None:
        self.ls.append(string)

    def to_string(self) -> str:
        return ''.join(self.ls)