from abc import ABC, abstractmethod


class Order(ABC):
    @abstractmethod
    def order_up(self) -> None:
        raise NotImplementedError
