from abc import ABC, abstractmethod
import random

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError
    
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket")

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        raise NotImplementedError
    
class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")

class Duck:
    fly_behavior: FlyBehavior = None
    quack_behavior: QuackBehavior = None

    def set_fly_behavior(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior):
        self.quack_behavior = quack_behavior

    def display(self):
        raise NotImplementedError
    
    def perform_fly(self) -> None:
        self.fly_behavior.fly()
        return None
    
    def perform_quack(self) -> None:
        self.quack_behavior.quack()
        return None
    
    def swim(self) -> None:
        print("All ducks float, even decoys")

class MallardDuck(Duck):
    fly_behavior = FlyWithWings()
    quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")

class ModelDuck(Duck):
    fly_behavior = FlyNoWay()
    quack_behavior = Squeak()

    def display(self):
        print("I'm a read Mallard duck")

def mini_duck_simulator():
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.perform_fly()
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()


class DuckAdapter:
    """Use duck to act like a turkey"""

    def __init__(self, duck: Duck):
        self.duck = duck
    
    def gobble(self):
        self.duck.perform_quack()

    def fly(self):
        if random.randint(0, 5) == 0:
            self.duck.perform_fly()

class TurkeyTestDrive:
    @staticmethod
    def main(*args):
        duck: Duck = MallardDuck()
        turkey: DuckAdapter = DuckAdapter(duck)

        for _ in range(10):
            print("The duck adapter says...")
            turkey.gobble()
            turkey.fly()

if __name__ == '__main__':
    mini_duck_simulator()
    TurkeyTestDrive.main()
