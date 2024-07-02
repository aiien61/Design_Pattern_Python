from abc import ABC
from typing import List

class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings: List[str]

    def get_name(self) -> str:
        return self.name
    
    def prepare(self) -> None:
        print(f"Preparing {self.name}")

    def bake(self) -> None:
        print(f"Baking {self.name}")

    def cut(self) -> None:
        print(f"Cutting {self.name}")

    def box(self) -> None:
        print(f"Boxing {self.name}")

    def to_string(self) -> str:
        display: StringBuffer = StringBuffer()
        display.append(f"----- {self.name} -----\n")
        display.append(f"{self.dough}\n")
        display.append(f"{self.sauce}\n")
        for topping in self.toppings:
            display.append(f"{topping}\n")
        return display.to_string()

class StringBuffer:
    def __init__(self):
        self.ls: List[str] = []

    def append(self, string: str):
        self.ls.append(string)

    def to_string(self) -> str:
        return ''.join(self.ls)