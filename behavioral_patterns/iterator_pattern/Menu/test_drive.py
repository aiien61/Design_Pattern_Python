from typing import Iterable, List

from menu import Menu
from menu_item import MenuItem
from diner_menu import DinerMenu
from pancake_house_menu import PancakeHouseMenu
from waitress import Waitress


class TestDrive:
    @staticmethod
    def main(*args, **kwargs):
        pancake_house_menu: Menu = PancakeHouseMenu()
        diner_menu: Menu = DinerMenu()
        waitress: Waitress = Waitress(diner_menu, pancake_house_menu)
        waitress.print_menu()
        waitress.print_vegetarian_menu()

        print("\nCustomer asks, is 椰香南瓜濃湯配麵包 vegetarian?")
        print("Waitress says: ", end="")
        if waitress.is_item_vegetarian("椰香南瓜濃湯配麵包"):
            print("Yes")
        else:
            print("No")

        print("\nCustomer asks, is 抹茶紅豆鬆餅 vegetarian?")
        print("Waitress says: ", end="")
        if waitress.is_item_vegetarian("抹茶紅豆鬆餅"):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    TestDrive.main()
