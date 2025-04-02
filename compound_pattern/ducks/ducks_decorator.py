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

class DuckSimulator:
    def simulate(self) -> None:
        mallard_duck: Quackable = QuackCounter(MallardDuck())
        redhead_duck: Quackable=QuackCounter(RedheadDuck())
        duck_call: Quackable = QuackCounter(DuckCall())
        rubber_duck: Quackable = QuackCounter(RubberDuck())
        goose_duck: Quackable = GooseAdapter(Goose())

        print("Duck Simulator")

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
        duck_simulator.simulate()
        return None


if __name__ == "__main__":
    TestDrive.main()
