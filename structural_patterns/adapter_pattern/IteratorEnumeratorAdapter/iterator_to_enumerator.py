from typing import List
from icecream import ic

class Enumeration:
    def __init__(self, data: List[object]):
        self.data: List[object] = data
        self.index: int = 0

    def has_more_elements(self) -> bool:
        return len(self.data) > self.index
    
    def next_element(self) -> object:
        if len(self.data) > self.index:
            temp: object = self.data[self.index]
            self.index += 1
            return temp
        return None
    
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
    
class IteratorToEnumerationAdapter(Enumeration):
    def __init__(self, iterator: Iterator):
        self.iterator = iterator
    
    def has_more_elements(self) -> bool:
        return self.iterator.has_next()
    
    def next_element(self) -> object:
        return self.iterator.get_next()
    
class EnumerationTestDrive:
    # ic.disable()

    @staticmethod
    def main(*args):
        iterator: Iterator = Iterator(['a', 'b', 'c'])
        enumerator: Enumeration = IteratorToEnumerationAdapter(iterator)
        while enumerator.has_more_elements():
            ic(enumerator.next_element())

if __name__ == '__main__':
    EnumerationTestDrive.main()
