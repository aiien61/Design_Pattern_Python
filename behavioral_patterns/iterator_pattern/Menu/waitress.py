from typing import Iterable

from menu import Menu
from menu_item import MenuItem


class Waitress:
    def __init__(self, diner_menu: Menu, pancake_house_menu: Menu):
        self.diner_menu = diner_menu
        self.pancake_house_menu = pancake_house_menu
    
    def print_menu(self):
        breakfast_items: Iterable[MenuItem] = self.pancake_house_menu.get_menu_items()
        print("MENU\n---\nBREAKFAST")
        for item in breakfast_items:
            self.print_menu_item(item)
        
        print("\nLUNCH")
        print("not implemented")

        print("\nDINNER")
        dinner_items: Iterable[MenuItem] = self.diner_menu.get_menu_items()
        for item in dinner_items:
            self.print_menu_item(item)


    def print_menu_item(self, menu_item: MenuItem) -> None:
        print(f"{menu_item.name}, {menu_item.price} -- {menu_item.description}\n")
