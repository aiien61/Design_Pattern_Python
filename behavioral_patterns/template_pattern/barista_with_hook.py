from abc import ABC, abstractmethod
from icecream import ic

class CaffeineBeverageWithHook(ABC):
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
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

    def customer_wants_condiments(self) -> bool:
        return True


class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self) -> None:
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

    def customer_wants_condiments(self):
        answer: str = self.__get_user_input()

        return True if answer.lower().startswith('y') else False
    
    def __get_user_input(self):
        answer: str = None
        try:
            answer = input("Would you like lemon with your tea (y/n)? ")
        except IOError:
            ic("IO error trying to read your answer")
        
        if answer is None:
            return "no"
        return answer

class CoffeeWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")

    def customer_wants_condiments(self):
        answer: str = self.__get_user_input()

        return True if answer.lower().startswith('y') else False
    
    def __get_user_input(self):
        answer: str = None
        try:
            answer = input("Would you like sugar and milk with your coffee (y/n)? ")
        except IOError:
            ic("IO error trying to read your answer")

        if answer is None:
            return "no"
        return answer


def beverage_test_drive():
    tea_hook: CaffeineBeverageWithHook = TeaWithHook()
    coffee_hook: CaffeineBeverageWithHook = CoffeeWithHook()

    print("\nMaking tea...")
    tea_hook.prepare_recipe()
    print("\nMaking coffee...")
    coffee_hook.prepare_recipe()

if __name__ == "__main__":
    beverage_test_drive()
