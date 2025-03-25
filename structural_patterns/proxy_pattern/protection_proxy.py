from abc import ABC, abstractmethod

class Driver:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class CarInterface(ABC):
    @abstractmethod
    def drive(self):
        raise NotImplementedError
    

class Car(CarInterface):
    def __init__(self, driver: Driver):
        self.driver = driver

    def drive(self):
        print(f'Car being driven by {self.driver.name}')


class CarProxy(CarInterface):
    def __init__(self, driver: Driver):
        self.driver = driver
        self.car = Car(self.driver)

    def drive(self):
        if self.driver.age < 18:
            print(f'Driver {self.driver.name} is too young')
        else:
            self.car.drive()

class TestDrive:
    @staticmethod
    def no_protection(*args, **kwargs):
        car = Car(Driver('Harry', 12))
        car.drive()

    @staticmethod
    def protection(*args, **kwargs):
        car = CarProxy(Driver('Harry', 12))
        car.drive()


if __name__ == '__main__':
    # TestDrive.no_protection()
    TestDrive.protection()
