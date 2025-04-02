from abc import ABC, abstractmethod
from rich import print

class Quackable(ABC):
    @abstractmethod
    def quack(self): raise NotImplementedError

class MallardDuck(Quackable):
    def quack(self) -> None:
        print("Quack")

class RedheadDuck(Quackable):
    def quack(self) -> None:
        print("Quack")

class DecoyDuck(Quackable):
    def quack(self) -> None:
        print("<< Silence >>")

class RubberDuck(Quackable):
    def quack(self) -> None:
        print("Squeak")

class DuckCall(Quackable):
    def quack(self) -> None:
        print("Kwak")

class DuckSimulator:
    def simulate(self) -> None:
        mallard_duck: Quackable = MallardDuck()
        redhead_duck: Quackable = RedheadDuck()
        duck_call: Quackable = DuckCall()
        rubber_duck: Quackable = RubberDuck()

        print("Duck Simulator")

        self._simulate(mallard_duck)
        self._simulate(redhead_duck)
        self._simulate(duck_call)
        self._simulate(rubber_duck)

    def _simulate(self, duck: Quackable) -> None:
        duck.quack()

class TestDrive:
    @staticmethod
    def main(*args) -> None:
        duck_simulator: DuckSimulator = DuckSimulator()
        duck_simulator.simulate()


if __name__ == "__main__":
    TestDrive.main()
