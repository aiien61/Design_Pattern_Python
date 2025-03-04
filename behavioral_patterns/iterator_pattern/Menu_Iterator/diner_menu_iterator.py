from typing import Iterator, List, Optional
from menu_item import MenuItem

class DinerMenuIterator(Iterator[MenuItem]):
    menu_list: List[MenuItem]
    position: int = 0

    def __init__(self, menu_list: List[MenuItem]):
        self.menu_list = menu_list

    def __next__(self) -> Optional[MenuItem]:
        if self.has_next():
            menu_item: MenuItem = self.menu_list[self.position]
            self.position += 1
            return menu_item
        raise StopIteration
    
    def has_next(self) -> bool:
        if self.position >= len(self.menu_list) or self.menu_list[self.position] == None:
            return False
        else:
            return True
        
    def remove(self) -> None:
        if self.position <= 0:
            raise NotImplementedError
        
        if self.menu_list[self.position - 1] != None:
            for i in range(self.position - 1, len(self.menu_list) - 1):
                self.menu_list[i] = self.menu_list[i + 1]
            self.menu_list[len(self.menu_list) - 1] = None
