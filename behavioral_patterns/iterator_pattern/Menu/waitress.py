from typing import Iterable, Iterator

from menu import Menu
from menu_item import MenuItem


class Waitress:
    def __init__(self, diner_menu: Menu, pancake_house_menu: Menu):
        self.diner_menu = diner_menu
        self.pancake_house_menu = pancake_house_menu
    
    def print_menu(self):
        breakfast_items: Iterable[MenuItem] = self.pancake_house_menu.get_menu_items()
        dinner_items: Iterable[MenuItem] = self.diner_menu.get_menu_items()

        print("MENU\n---\nBREAKFAST")
        for item in breakfast_items:
            self._print_menu_item(item)
        
        print("\nLUNCH")
        print("not implemented")

        print("\nDINNER")
        for item in dinner_items:
            self._print_menu_item(item)

    def _print_menu_item(self, menu_item: MenuItem) -> None:
        print(f"{menu_item.name}, {menu_item.price} -- {menu_item.description}\n")

    def print_vegetarian_menu(self) -> None:
        print("\nVEGETARIAN MENU\n---\nBREAKFAST")
        self._print_vegetarian_menu(self.pancake_house_menu.create_iterator())

        print("\nLUNCH")
        print("not implemented")

        print("\nDINNER")
        self._print_vegetarian_menu(self.diner_menu.create_iterator())

    def is_item_vegetarian(self, name: str) -> bool:
        if self._is_vegetarian(name, self.pancake_house_menu.create_iterator()):
            return True
        if self._is_vegetarian(name, self.diner_menu.create_iterator()):
            return True
        return False
    
    def _print_vegetarian_menu(self, iterator: Iterator) -> None:
        menu_item: MenuItem = next(iterator, None)
        while menu_item:
            if menu_item.is_vegetarian():
                self._print_menu_item(menu_item)
            menu_item = next(iterator, None)

    def _is_vegetarian(self, name: str, iterator: Iterator) -> bool:
        menu_item: MenuItem = next(iterator, None)
        while menu_item:
            if menu_item.get_name() == name and menu_item.is_vegetarian():
                return True
            menu_item = next(iterator, None)
        return False
