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


class Goose:
    def honk(self) -> None:
        print("Honk")


class GooseAdapter(Quackable):
    def __init__(self, goose: Goose):
        self.goose = Goose()
    
    def quack(self) -> None:
        self.goose.honk()

    def __str__(self) -> str:
        return "Goose pretending to be a Duck"
    
    def __repr__(self) -> str:
        return str(self)


class DuckSimulator:
    def simulate(self) -> None:
        mallard_duck: Quackable = MallardDuck()
        redhead_duck: Quackable = RedheadDuck()
        duck_call: Quackable = DuckCall()
        rubber_duck: Quackable = RubberDuck()
        goose_duck: Quackable = GooseAdapter(Goose())

        print("Duck Simulator: With Goose Adapter")

        self._simulate(mallard_duck)
        self._simulate(redhead_duck)
        self._simulate(duck_call)
        self._simulate(rubber_duck)
        self._simulate(goose_duck)
    
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
