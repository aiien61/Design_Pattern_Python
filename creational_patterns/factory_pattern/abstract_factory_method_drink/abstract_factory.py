from enum import Enum, auto
from abc import ABC, abstractmethod
from typing import List, Dict

class HotDrink(ABC):
    @abstractmethod
    def consume(self): raise NotImplementedError


class Tea(HotDrink):
    def consume(self):
        print("This tea is delicious")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious")


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount: int): raise NotImplementedError


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount: int):
        print(f"Put in tea bag, boil water, pour {amount} ml, enjoy!")
        return Tea()
    
class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount: int):
        print(f"Grind some beans, boil water, pour {amount} ml, enjoy!")
        return Coffee()


def make_a_drink(type: str) -> HotDrink:
    if type == "tea":
        return TeaFactory().prepare(200)
    elif type == "coffee":
        return CoffeeFactory().prepare(50)
    else:
        return None
    

class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories: Dict[str, HotDrinkFactory] = {}
    initialized: bool = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                drink_name = d.name.title()
                factory_name = drink_name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories[drink_name] = factory_instance
    
    def make_a_drink(self):
        print("Available drinks:")
        for drink_name in self.factories.keys():
            print(drink_name)
        
        drink_name: str = input(f"Please pick drink: ").title()
        drink_amount: int = int(input("Specify amount: "))
        return self.factories[drink_name].prepare(drink_amount)
        

if __name__ == "__main__":
    # user_choice = input("What kind of drink would you like? [Tea/Coffee]: ").lower()
    # drink = make_a_drink(user_choice)
    # drink.consume()

    drink_machine = HotDrinkMachine()
    drink_machine.make_a_drink()
