from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Pizza:
    name: str
    topping: List[str]

    def add_toppings(self, toppings: List[str]) -> None:
        self.toppings = toppings

    def prepare(self) -> None:
        print(f"Prepare {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings...")
        for topping in self.toppings:
            print(f"    {topping}")

    def bake(self) -> None:
        print("Bake for 25 minutes at 350")
    
    def cut(self) -> None:
        print("Cut the pizza into diagonal slices")

    def box(self) -> None:
        print("Place pizza in official PizzaStore box")

    def set_name(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        ls = []
        ls.append(f"{self.name} with [")
        for idx, topping in enumerate(self.toppings):
            if idx < len(self.toppings) - 1:
                ls.append(f"{topping}, ")
            else:
                ls.append(f"{topping}]")
        
        return ''.join(ls)
    
    def __repr__(self) -> str:
        return str(self)


class PizzaBuilder(ABC):
    name: str
    toppings: List[str]

    @abstractmethod
    def add_cheese(self) -> PizzaBuilder: pass

    @abstractmethod
    def add_sauce(self) -> PizzaBuilder: pass

    @abstractmethod
    def add_tomatoes(self) -> PizzaBuilder: pass

    @abstractmethod
    def add_garlic(self) -> PizzaBuilder: pass

    @abstractmethod
    def add_olives(self) -> PizzaBuilder: pass

    @abstractmethod
    def add_spinach(self) -> PizzaBuilder: pass

    @abstractmethod
    def add_pepperoni(self) -> PizzaBuilder: pass

    @abstractmethod
    def add_sausage(self) -> PizzaBuilder: pass

    def build(self) -> Pizza:
        pizza: Pizza = Pizza()
        pizza.set_name(self.name)
        pizza.add_toppings(self.toppings)
        return pizza


class VeggieLoversPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.name: str = "Veggie Lovers Pizza"
        self.toppings: List[str] = []

    def add_cheese(self) -> PizzaBuilder:
        self.toppings.append("parmesan")
        return self
    
    def add_sauce(self):
        self.toppings.append("sauce")
        return self
    
    def add_tomatoes(self):
        self.toppings.append("chopped tomatoes")
        return self
    
    def add_garlic(self):
        self.toppings.append("garlic")
        return self
    
    def add_olives(self):
        self.toppings.append("green olives")
        return self
    
    def add_spinach(self):
        self.toppings.append("spinach")
        return self
    
    def add_pepperoni(self):
        return self
    
    def add_sausage(self):
        return self


class MeatLoversPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.name: str = "Meat Lovers Pizza"
        self.toppings: List[str] = []

    def add_cheese(self) -> PizzaBuilder:
        self.toppings.append("mozzerela")
        return self

    def add_sauce(self):
        self.toppings.append("authentic Italian sauce")
        return self

    def add_tomatoes(self):
        self.toppings.append("sliced tomatoes")
        return self

    def add_garlic(self):
        self.toppings.append("garlic")
        return self

    def add_olives(self):
        return self

    def add_spinach(self):
        return self

    def add_pepperoni(self):
        self.toppings.append("pepperoni")
        return self

    def add_sausage(self):
        self.toppings.append("sausage")
        return self


class StringBuilder:
    def __init__(self):
        self.ls = []

    def append(self, string: str) -> None:
        self.ls.append(string)

    def to_string(self) -> str:
        return ''.join(self.ls)
    
    def __len__(self) -> int:
        return sum(map(len, self.ls))
    
    def __setitem__(self, idx, value) -> None:
        self.ls[idx] = value

class PizzaDirector:
    @staticmethod
    def main(*args):
        veggie_builder: PizzaBuilder = VeggieLoversPizzaBuilder()
        veggie: Pizza = veggie_builder.add_sauce().add_cheese().add_olives().add_tomatoes().add_sausage().build()
        veggie.prepare()
        veggie.bake()
        veggie.cut()
        veggie.box()
        print(veggie)

        meat_builder: PizzaBuilder = MeatLoversPizzaBuilder()
        meat: Pizza = meat_builder.add_sauce().add_tomatoes().add_cheese().add_sausage().add_pepperoni().build()
        meat.prepare()
        meat.bake()
        meat.cut()
        meat.box()
        print(meat)

        sb: StringBuilder = StringBuilder()
        sb.append("\nTesting String Builder\n")
        sb.append(str(veggie))
        sb[0] = "\n===="
        print(f"Length of the String Builder: {len(sb)}")
        print(f"Result of the Sring Builder: {sb.to_string()}")

        sb2: StringBuilder = StringBuilder()
        sb2.append("\nTesting String Builder\n")
        sb2.append(str(meat))
        sb2[0] = "\n===="
        sb2: str = sb2.to_string()
        print(sb2)

if __name__ == "__main__":
    PizzaDirector.main()