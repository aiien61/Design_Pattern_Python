class CEO:
    __shared_state: dict = {'name': 'John', 'age': 50}

    def __init__(self) -> None:
        self.__dict__ = self.__shared_state

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"
    
class Monostate:
    _shared_state: dict = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

class CFO(Monostate):
    def __init__(self) -> None:
        self.name = ''
        self.money_managed = 0

    def __str__(self) -> str:
        return f'CFO {self.name} manages ${self.money_managed}'

if __name__ == '__main__':
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.age = 70
    print(ceo1)
    print(ceo2)

    cfo1 = CFO()
    cfo1.name = 'Mark'
    cfo1.money_managed = 1000
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = 'Rob'
    cfo2.money_managed = 2000
    print(cfo1, cfo2, sep='\n')