from abc import ABC, abstractmethod

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self): raise NotImplementedError
    @abstractmethod
    def __str__(self): raise NotImplementedError

class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying.")

    def __str__(self): return 'FlyWithWings'

class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("I can't fly.")

    def __str__(self): return 'FlyNoWay'

class FlyRocketPowered(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying with a rocket.")

    def __str__(self): return 'FlyRocketPowered'

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self): raise NotImplementedError
    @abstractmethod
    def __str__(self): raise NotImplementedError

class Quack(QuackBehavior):
    def quack(self):
        print('Quack')
    
    def __str__(self): return 'Quack'

class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print('<< Silence >>')

    def __str__(self): return 'MuteQuack'

class Squeak(QuackBehavior):
    def quack(self) -> None:
        print('Squeak')

    def __str__(self): return 'Squeak'

class Duck(ABC):
    _fly_behavior: FlyBehavior = None
    _quck_behavior: QuackBehavior = None

    @property
    def fly_behavior(self): return self._fly_behavior
    
    @fly_behavior.setter
    def fly_behavior(self, fly_behavior: FlyBehavior):
        print(f'{self} changed the fly behavior from {self.fly_behavior} to {fly_behavior}')
        self._fly_behavior = fly_behavior

    @property
    def quack_behavior(self): return self._quck_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior: QuackBehavior):
        print(f'{self} changed the quack behavior from {self.quack_behavior} to {quack_behavior}')
        self._quck_behavior = quack_behavior

    @abstractmethod
    def display(self): 
        raise NotImplementedError
    
    def perform_fly(self) -> None:
        self._fly_behavior.fly()

    def perform_quack(self) -> None:
        self._quck_behavior.quack()

    def swim(self) -> None:
        print('All ducks float, even decoys.')

    @abstractmethod
    def __str__(self): raise NotImplementedError

class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print("I'm a real Mallard duck.")

    def __str__(self):
        return 'Mallard duck'

class DecoyDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def display(self) -> None:
        print("I'm a duck decoy.")

    def __str__(self):
        return 'Decoy duck'

class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self) -> None:
        print("I'm a model duck.")

    def __str__(self):
        return 'Model duck'

class RedHeadDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print("I'm a real Red Headed duck.")

    def __str__(self):
        return 'Red headed duck'

class RubberDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self) -> None:
        print("I'm a rubber duckie.")

    def __str__(self):
        return 'Rubber duck'

def mini_duck_simulator():
    mallard = MallardDuck()
    mallard.display()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.fly_behavior = FlyRocketPowered()
    model.perform_fly()


if __name__ == '__main__':
    mini_duck_simulator()
