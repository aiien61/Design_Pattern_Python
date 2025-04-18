from abc import ABC, abstractmethod
from rich import print
from typing import List


class Quackable(ABC):
    @abstractmethod
    def quack(self): raise NotImplementedError


class MallardDuck(Quackable):
    def quack(self) -> None:
        print("Quack")

    def __str__(self) -> str:
        return "Mallard Duck"

    def __repr__(self):
        return str(self)


class RedheadDuck(Quackable):
    def quack(self) -> None:
        print("Quack")

    def __str__(self) -> str:
        return "Redhead Duck"

    def __repr__(self):
        return str(self)


class DecoyDuck(Quackable):
    def quack(self) -> None:
        print("<< Silence >>")

    def __str__(self) -> str:
        return "Decoy Duck"

    def __repr__(self):
        return str(self)


class RubberDuck(Quackable):
    def quack(self) -> None:
        print("Squeak")

    def __str__(self) -> str:
        return "Rubber Duck"

    def __repr__(self):
        return str(self)


class DuckCall(Quackable):
    def quack(self) -> None:
        print("Kwak")

    def __str__(self) -> str:
        return "Duck Call"

    def __repr__(self):
        return str(self)


class Goose:
    def honk(self) -> None:
        print("Honk")

    def __str__(self) -> str:
        return "Goose"

    def __repr__(self):
        return str(self)


class GooseAdapter(Quackable):
    def __init__(self, goose: Goose):
        self.goose = Goose()

    def quack(self) -> None:
        self.goose.honk()

    def __str__(self) -> str:
        return "Goose pretending to be a Duck"

    def __repr__(self) -> str:
        return str(self)


class QuackCounter(Quackable):
    number_of_quacks: List[int] = [0]

    def __init__(self, duck: Quackable):
        self.duck = duck

    def quack(self) -> None:
        self.duck.quack()
        self.number_of_quacks[0] += 1

    @staticmethod
    def get_quacks() -> int:
        return QuackCounter.number_of_quacks[0]

    def __str__(self) -> str:
        return str(self.duck)

    def __repr__(self) -> str:
        return repr(self.duck)
    

class AbstractDuckFactory(ABC):
    @abstractmethod
    def create_mallard_duck(self) -> Quackable:
        raise NotImplementedError

    @abstractmethod
    def create_redhead_duck(self) -> Quackable:
        raise NotImplementedError

    @abstractmethod
    def create_duck_call(self) -> Quackable:
        raise NotImplementedError

    @abstractmethod
    def create_rubber_duck(self) -> Quackable:
        raise NotImplementedError


class CountingDuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self) -> Quackable:
        return QuackCounter(MallardDuck())
    
    def create_redhead_duck(self) -> Quackable:
        return QuackCounter(RedheadDuck())
    
    def create_duck_call(self) -> Quackable:
        return QuackCounter(DuckCall())
    
    def create_rubber_duck(self) -> Quackable:
        return QuackCounter(RubberDuck())

class DuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self) -> Quackable:
        return MallardDuck()
    
    def create_redhead_duck(self) -> Quackable:
        return RedheadDuck()
    
    def create_rubber_duck(self) -> Quackable:
        return DuckCall()
    
    def create_duck_call(self) -> Quackable:
        return RubberDuck()

class DuckSimulator:
    def simulate(self, duck_factory: AbstractDuckFactory) -> None:
        mallard_duck: Quackable = duck_factory.create_mallard_duck()
        redhead_duck: Quackable = duck_factory.create_redhead_duck()
        duck_call: Quackable = duck_factory.create_duck_call()
        rubber_duck: Quackable = duck_factory.create_rubber_duck()
        goose_duck: Quackable = GooseAdapter(Goose())

        print("\nDuck Simulator: With Abstract Factory")

        self._simulate(mallard_duck)
        self._simulate(redhead_duck)
        self._simulate(duck_call)
        self._simulate(rubber_duck)
        self._simulate(goose_duck)

        print(f"The ducks quacked {QuackCounter.get_quacks()} times")

    def _simulate(self, duck: Quackable) -> None:
        duck.quack()
        return None


class TestDrive:
    @staticmethod
    def main(*args) -> None:
        duck_simulator: DuckSimulator = DuckSimulator()
        duck_factory: AbstractDuckFactory = CountingDuckFactory()
        duck_simulator.simulate(duck_factory)
        return None


if __name__ == "__main__":
    TestDrive.main()
