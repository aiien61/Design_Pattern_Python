class ChocolateBoiler:
    __empty: bool
    __boiled: bool
    __unique_instance: 'ChocolateBoiler' = None

    def __init__(self):
        self.__empty = True
        self.__boiled = False

    @staticmethod
    def get_instance() -> 'ChocolateBoiler':
        if ChocolateBoiler.__unique_instance is None:
            print('Creating unique instance of ChocolateBoiler')
            ChocolateBoiler.__unique_instance = ChocolateBoiler()
        return ChocolateBoiler.__unique_instance
    
    def is_empty(self) -> bool:
        return self.__empty

    def is_boiled(self) -> bool:
        return self.__boiled
    
    def fill(self) -> None:
        if self.is_empty():
            self.__empty = False
            self.__boiled = False
    
    def drain(self) -> None:
        if not self.is_empty() and self.is_boiled():
            self.__empty = True

    def boil(self) -> None:
        if not self.is_empty() and not self.is_boiled():
            self.__boiled = True

class ChocolateController:
    @staticmethod
    def main() -> None:
        print('Get a chocolate boiler 1')
        boiler1: ChocolateBoiler = ChocolateBoiler.get_instance()
        print(f"boiler1 is empty: {boiler1.is_empty()}")
        print(f"boiler1 is boiled: {boiler1.is_boiled()}")
        boiler1.fill()
        boiler1.boil()

        print('Get a chocolate boiler 2')
        boiler2: ChocolateBoiler = ChocolateBoiler.get_instance()
        print(f"boiler2 is empty: {boiler2.is_empty()}")
        print(f"boiler2 is boiled: {boiler1.is_boiled()}")
        print(boiler1 is boiler2)
        boiler2.drain()
        print(f"boiler2 is empty: {boiler2.is_empty()}")

if __name__ == '__main__':
    ChocolateController.main()