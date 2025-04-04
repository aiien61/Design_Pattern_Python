from abc import ABC, abstractmethod
from rich import print
from typing import List, Iterator


class Quackable(ABC):
    @abstractmethod
    def quack(self): raise NotImplementedError


class Observer(ABC):
    @abstractmethod
    def update(self, duck: Quackable) -> None:
        pass


class QuackObservable(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class Observable(QuackObservable):
    observers: List[Observer] = []
    duck: QuackObservable

    def __init__(self, duck: QuackObservable):
        self.duck = duck
        self.observers = []

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def notify_observers(self) -> None:
        iterator: Iterator[Observer] = iter(self.observers)
        observer: Observer = next(iterator, None)
        while observer is not None:
            observer.update(self.duck)
            observer: Observer = next(iterator, None)
        return None

    def get_observers(self) -> Iterator[Observer]:
        return iter(self.observers) 


class MallardDuck(Quackable):
    observable: Observable

    def __init__(self):
        self.observable = Observable(self)

    def quack(self) -> None:
        print("Quack")
        self.notify_observer()
    
    def register_observer(self, observer: Observer) -> None:
        self.observable.register_observer(observer)

    def notify_observer(self) -> None:
        self.observable.notify_observers()

    def __str__(self) -> str:
        return "Mallard Duck"

    def __repr__(self):
        return str(self)


class RedheadDuck(Quackable):
    observable: Observable

    def __init__(self):
        self.observable = Observable(self)

    def quack(self) -> None:
        print("Quack")
        self.notify_observer()

    def register_observer(self, observer: Observer) -> None:
        self.observable.register_observer(observer)

    def notify_observer(self) -> None:
        self.observable.notify_observers()

    def __str__(self) -> str:
        return "Redhead Duck"

    def __repr__(self):
        return str(self)


class DecoyDuck(Quackable):
    observable: Observable

    def __init__(self):
        self.observable = Observable(self)

    def quack(self) -> None:
        print("<< Silence >>")
        self.notify_observer()

    def register_observer(self, observer: Observer) -> None:
        self.observable.register_observer(observer)
    
    def notify_observer(self) -> None:
        self.observable.notify_observers()


    def __str__(self) -> str:
        return "Decoy Duck"

    def __repr__(self):
        return str(self)


class RubberDuck(Quackable):
    observable: Observable

    def __init__(self):
        self.observable = Observable(self)

    def quack(self) -> None:
        print("Squeak")
        self.notify_observer()

    def register_observer(self, observer: Observer) -> None:
        self.observable.register_observer(observer)

    def notify_observer(self) -> None:
        self.observable.notify_observers()

    def __str__(self) -> str:
        return "Rubber Duck"

    def __repr__(self):
        return str(self)


class DuckCall(Quackable):
    observable: Observable

    def __init__(self):
        self.observable = Observable(self)

    def quack(self) -> None:
        print("Kwak")
        self.notify_observer()

    def register_observer(self, observer: Observer) -> None:
        self.observable.register_observer(observer)

    def notify_observer(self) -> None:
        self.observable.notify_observers()

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
    goose: Goose
    observable: Observable

    def __init__(self, goose: Goose):
        self.goose = goose
        self.observable = Observable(self)

    def quack(self) -> None:
        self.goose.honk()
        self.notify_observer()

    def register_observer(self, observer: Observer) -> None:
        self.observable.register_observer(observer)

    def notify_observer(self) -> None:
        self.observable.notify_observers()


    def __str__(self) -> str:
        return "Goose pretending to be a Duck"

    def __repr__(self) -> str:
        return str(self)


class QuackCounter(Quackable):
    duck: Quackable
    number_of_quacks: List[int] = [0]

    def __init__(self, duck: Quackable):
        self.duck = duck

    def quack(self) -> None:
        self.duck.quack()
        self.number_of_quacks[0] += 1

    @staticmethod
    def get_quacks() -> int:
        return QuackCounter.number_of_quacks[0]
    
    def register_observer(self, observer: Observer) -> None:
        self.duck.register_observer(observer)

    def notify_observers(self) -> None:
        self.duck.notify_observers()

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


class Flock(Quackable):
    quackers: List[Quackable]

    def __init__(self):
        self.quackers = []

    def add(self, quacker: Quackable) -> None:
        self.quackers.append(quacker)
        return None

    def quack(self) -> None:
        iterator: Iterator[Quackable] = iter(self.quackers)
        quacker: Quackable = next(iterator, None)
        while quacker is not None:
            quacker.quack()
            quacker: Quackable = next(iterator, None)
        return None
    
    def register_observer(self, observer: Observer) -> None:
        iterator: Iterator[Quackable] = iter(self.quackers)
        quacker: Quackable = next(iterator, None)
        while quacker is not None:
            quacker.register_observer(observer)
            quacker: Quackable = next(iterator, None)
        return None

    def __str__(self) -> str:
        return "Flock of Quackers"

    def __repr__(self) -> str:
        return str(self)
    

class Quackologist(Observer):
    def update(self, quacker: QuackObservable) -> None:
        print(f"Quackologist: {quacker} just quacked")

    def __str__(self) -> str:
        return "Quackologist"
    
    def __repr__(self) -> str:
        return str(self)


class DuckSimulator:
    def simulate(self, duck_factory: AbstractDuckFactory) -> None:
        mallard_duck: Quackable = duck_factory.create_mallard_duck()
        redhead_duck: Quackable = duck_factory.create_redhead_duck()
        duck_call: Quackable = duck_factory.create_duck_call()
        rubber_duck: Quackable = duck_factory.create_rubber_duck()
        goose_duck: Quackable = GooseAdapter(Goose())

        print("\nDuck Simulator: With Composite - Flocks")

        flock_of_ducks: Flock = Flock()

        flock_of_ducks.add(redhead_duck)
        flock_of_ducks.add(duck_call)
        flock_of_ducks.add(rubber_duck)

        flock_of_mallard_ducks: Flock = Flock()

        mallard1: Quackable = duck_factory.create_mallard_duck()
        mallard2: Quackable = duck_factory.create_mallard_duck()
        mallard3: Quackable = duck_factory.create_mallard_duck()
        mallard4: Quackable = duck_factory.create_mallard_duck()
        mallard5: Quackable = duck_factory.create_mallard_duck()

        flock_of_mallard_ducks.add(mallard1)
        flock_of_mallard_ducks.add(mallard2)
        flock_of_mallard_ducks.add(mallard3)
        flock_of_mallard_ducks.add(mallard4)
        flock_of_mallard_ducks.add(mallard5)

        flock_of_ducks.add(flock_of_mallard_ducks)

        print("\nDuck Simulator: With Observer")
        quackologist: Quackologist = Quackologist()
        flock_of_ducks.register_observer(quackologist)

        self._simulate(flock_of_ducks)

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
