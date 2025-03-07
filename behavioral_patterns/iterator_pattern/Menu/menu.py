from typing import Iterator
from abc import ABC, abstractmethod
from menu_item import MenuItem

# aggregator interface
class Menu(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator[MenuItem]:
        raise NotImplementedError
