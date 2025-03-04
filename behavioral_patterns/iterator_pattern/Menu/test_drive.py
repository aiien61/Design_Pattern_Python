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

if __name__ == '__main__':
    TestDrive.main()
