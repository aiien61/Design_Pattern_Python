from abc import ABC, abstractmethod
from enum import Enum, auto


class BeverageSize:
    """Starbuzz sizes for coffees. 
    TALL is the smallest size. 
    GRANDE is the medium/normal size.
    VENTI is the large one.
    """
    TALL = auto()
    GRANDE = auto()
    VENTI = auto()


class Beverage(ABC):
    """Base class for all beverages."""
    _size: BeverageSize = BeverageSize.TALL
    _description: str = "Unknown Beverage"

    @property
    def description(self) -> str: return self._description

    @property
    def size(self) -> BeverageSize: return self._size

    @size.setter
    def size(self, new_size: BeverageSize) -> None:
        self._size = new_size

    @abstractmethod
    def cost(self) -> float: raise NotImplementedError
    

class CondimentDecorator(Beverage, ABC):
    beverage: Beverage

    @property
    def size(self) -> BeverageSize: return self.beverage.size


class Espresso(Beverage):
    _description: str = "Espresso"

    def cost(self) -> float: return 1.99


class HouseBlend(Beverage):
    _description: str = "House Blend Coffee"

    def cost(self) -> float: return 0.89


class DarkRoast(Beverage):
    _description: str = "Dark Roast Coffee"

    def cost(self) -> float: return 0.99


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    @property
    def description(self) -> str: return self.beverage.description + ', Mocha'

    def cost(self) -> float: return self.beverage.cost() + 0.20


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    @property
    def description(self) -> str: return self.beverage.description + ', Whip'

    def cost(self) -> float: return self.beverage.cost() + 0.1


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    @property
    def description(self) -> str: return self.beverage.description + ', Soy'

    def cost(self) -> float: 
        extra_cost: float = 0.15
        if self.beverage.size == BeverageSize.TALL:
            extra_cost = 0.10
        elif self.beverage.size == BeverageSize.GRANDE:
            extra_cost = 0.15
        elif self.beverage.size == BeverageSize.VENTI:
            extra_cost = 0.20
        return self.beverage.cost() + extra_cost


class StartbuzzCoffee:
    @staticmethod
    def main(*args) -> None:
        beverage: Beverage = Espresso()
        print(f'{beverage.description} ${beverage.cost()}')

        beverage2: Beverage = DarkRoast()
        beverage2 = Mocha(beverage2)
        beverage2 = Mocha(beverage2)
        beverage2 = Whip(beverage2)
        print(f'{beverage2.description} ${beverage2.cost()}')

        beverage3: Beverage = HouseBlend()
        beverage3 = Soy(beverage3)
        beverage3 = Mocha(beverage3)
        beverage3 = Whip(beverage3)
        print(f'{beverage3.description} ${beverage3.cost()}')

        beverage4: Beverage = HouseBlend()
        beverage4.size = BeverageSize.GRANDE
        beverage4 = Soy(beverage4)
        beverage4 = Mocha(beverage4)
        beverage4 = Whip(beverage4)
        print(f'{beverage4.description} ${beverage4.cost()}')



if __name__ == '__main__':
    StartbuzzCoffee.main()