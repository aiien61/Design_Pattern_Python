"""Interface Segregation Principle 介面隔離原則: similar with single responsibility principle. 
1. Don't put too much into an interface; split into separate interfaces.
2. YAGNI
3. Suggesting that a big interface can be divided into many small interfaces, in order for users to 
focus on the interface that is most relevant to their business logic.

Advantages: 
1. decoupling classes, i.e. reducing the dependency between classes, to increase the flexibility and
maintainability of the code.
2. users can focus on the interfaces that are most relevant to their business logic, so don't need
to be concerned about the big, whole interface that increase the complexity of the code.
"""

from abc import abstractmethod


"""
Case: Printer Machine
"""
class Machine:
    def print(self, document):
        raise NotImplementedError
    
    def scan(self, document):
        raise NotImplementedError
    
    def fax(self, document):
        raise NotImplementedError
    
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

class OldFashionedPrinter(Machine):
    def print(self, document):
        # it's ok to have this method
        pass

    # it doesn't make sense to have this method in an old fashioned printer, either to be able to raise error
    # because users can also have chance to invoke it by API. However, it must be implemented at the
    # same time because it's an abstract method from base class, so this subclass interface segregation principle
    def fax(self, document):
        pass

    # it doesn't make sense to have this method in an old fashioned printer, either to be able to raise error
    # because users can also have chance to invoke it by API. However, it must be implemented at the
    # same time because it's an abstract method from base class, so this subclass interface segregation principle
    def scan(self, document):
        '''Not Supported'''
        raise NotImplementedError('Printer cannot scan!')
    
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass

class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


"""
Case: Figure Shape
"""
class Shape:
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor):
        pass

class Rectangle(Shape):
    def draw(self):
        print('Drawing a rectangle')
    
    def resize(self, factor):
        print(f'Resizing the rectangle by {factor}')

class Circle(Shape):
    def draw(self):
        print('Drawing a circle')

    def resize(self, factor):
        print(f'Resizing the circle by {factor}')


"""
Incorrect Case: Animal
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def swim(self):
        print(f'{self.name} is swimming')

    def fly(self):
        print(f'{self.name} is flying')

class Fish(Animal):
    def fly(self):
        print('Error: Fishes cannot fly')

class Bird(Animal):
    def swim(self):
        print('Error: Birds cannot swim')


"""
Fixed Case: Animal
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

class Swimmer:
    def swim(self):
        pass

class Flyer:
    def fly(self):
        pass

class Fish(Animal, Swimmer):
    def swim(self):
        print(f'{self.name} is swimming')

class Bird(Animal, Flyer):
    def fly(self):
        print(f'{self.name} is flying')


if __name__ == '__main__':
    rectangle = Rectangle()
    circle = Circle()
    
    rectangle.draw()
    rectangle.resize(2)

    circle.draw()
    circle.resize(1.5)

    bird = Bird('Parrot')
    bird.fly()

    fish = Fish('Nemo')
    fish.swim()