from typing import List
from icecream import ic

class Iterator:
    def __init__(self, data: List[object]):
        self.data: List[object] = data
        self.index: int = 0

    def has_next(self) -> bool:
        return len(self.data) > self.index

    def get_next(self) -> object:
        if len(self.data) > self.index:
            temp: object = self.data[self.index]
            self.index += 1
            return temp
        
        return None
    
class Enumeration:
    def __init__(self, data: List[object]) -> None:
        self.data: List[object] = data
        self.index: int = 0

    def has_more_elements(self) -> bool:
        return len(self.data) > self.index
    
    def next_element(self) -> object:
        if len(self.data) > self.index:
            temp = self.data[self.index]
            self.index += 1
            return temp
        return None
    
class UnsupportedOperationException(Exception):
    pass

class EnumerationToIteratorAdapter(Iterator):
    def __init__(self, enumeration: Enumeration):
        self.enumeration = enumeration

    def has_next(self) -> bool:
        return self.enumeration.has_more_elements()
    
    def get_next(self) -> object:
        return self.enumeration.next_element()
    
    def remove(self) -> None:
        raise UnsupportedOperationException

class IteratorTestDrive:
    # ic.disable()

    @staticmethod
    def main(*args):
        enumerator: Enumeration = Enumeration(['a', 'b', 'c'])
        iterator: Iterator = EnumerationToIteratorAdapter(enumerator)
        while iterator.has_next():
            ic(iterator.get_next())
            
if __name__ == '__main__':
    IteratorTestDrive.main()