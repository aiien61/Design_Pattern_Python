from abc import ABC, abstractmethod


class Turkey(ABC):
    @abstractmethod
    def gobble(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError


class WildTurkey(Turkey):
    def gobble(self) -> None:
        print('Gobble gobble')

    def fly(self) -> None:
        print("I'm flying a short distance")