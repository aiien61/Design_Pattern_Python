class SingletonError(Exception):
    pass

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    

class ChocolateBoiler(metaclass=Singleton):
    def __init__(self):
        self.empty: bool = True
        self.boiled: bool = False

    def fill(self) -> None:
        if not self.empty:
            raise SingletonError
        self.empty = False
        self.boiled = False
        print('Full!')

    def drain(self) -> None:
        if self.empty or (not self.boiled):
            raise SingletonError
        self.empty = True
        print('Empty!')

    def boil(self) -> None:
        self.boild = True
        print('Boiled!')

    def is_empty(self) -> bool:
        return self.empty
    
    def is_boiled(self) -> bool:
        return self.boiled
    

def chocolate_controller():
    boiler1: ChocolateBoiler = ChocolateBoiler()
    print(f"boiler1 is empty: {boiler1.is_empty()}", )
    print("fill and boilboiler1 ")
    boiler1.fill()
    boiler1.boil()
    boiler2: ChocolateBoiler = ChocolateBoiler()
    print(f"boiler2 is empty: {boiler2.is_empty()}")
    print(f"boiler1 is boiled: {boiler1.is_boiled()}")
    print(boiler1 is boiler2)

if __name__ == '__main__':
    chocolate_controller()