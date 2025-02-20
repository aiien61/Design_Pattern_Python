from abc import ABC, abstractmethod

class CaffeineBeverage(ABC):
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def add_condiments(self) -> None:
        raise NotImplementedError
    
    def boil_water(self) -> None:
        print("Boiling water")

    def pour_in_cup(self) -> None:
        print("Pouring into cup")

class Tea(CaffeineBeverage):
    def brew(self) -> None:
        print("Steeping the tea")

    def add_condiments(self) -> None:
        print("Adding lemon")

class Coffee(CaffeineBeverage):
    def brew(self) -> None:
        print("Dripping coffee through filter")

    def add_condiments(self) -> None:
        print("Adding sugar and milk")

def beverage_test_drive():
    tea = Tea()
    coffee = Coffee()
    print("\nMaking tea...")
    tea.prepare_recipe()
    print("\nMaking coffee...")
    coffee.prepare_recipe()

if __name__ == "__main__":
    beverage_test_drive()
