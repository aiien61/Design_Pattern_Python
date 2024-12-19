from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError
    
    @abstractmethod
    def undo(self):
        raise NotImplementedError
