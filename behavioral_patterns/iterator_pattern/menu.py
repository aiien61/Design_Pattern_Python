from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class MenuItem:
    name: str
    description: str
    vegetarian: bool
    price: float

class Menu(ABC):
    @abstractmethod
    def __iter__(self):
        raise NotImplementedError
    
class CafeMenu(Menu):
    def __init__(self):
        self.menu_items: Dict[str, MenuItem] = {}
        self.add_item(
            "素食黑豆漢堡",
            "以黑豆與蔬菜製成的素肉餅，搭配酪梨醬、生菜與番茄，清爽又營養。",
            True,
            150
        )

        self.add_item(
            "起司薯條",
            "金黃酥脆的薯條，淋上濃濃的溫熱起司醬，簡單卻令人滿足的速食經典。",
            True,
            120
        )

        self.add_item(
            "BBQ豬肋排套餐",
            "慢烤至軟嫩的豬肋排，刷上濃郁的燒烤醬，搭配薯條與玉米沙拉，份量十足的美式風情",
            False,
            280
        )

    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        self.menu_items[name] = MenuItem(name, description, vegetarian, price)
        return None
    
    def __iter__(self):
        return iter(self.menu_items.values())
    
class DinerMenu(Menu):
    def __init__(self):
        self.menu_items: List[MenuItem] = []
        self.add_item(
            "法式鴨胸佐橙酒醬",
            "外皮酥脆、內裡粉嫩的鴨胸，搭配濃郁橙酒醬汁與焦糖橙片，佐以百里香烤小土豆，酸甜與肉香完美平衡。",
            False,
            1_200,
        )

        self.add_item(
            "松露奶油蘑菇燉飯",
            "使用義大利阿博利歐米與新鮮松露，慢煮於濃郁奶油與白酒中，撒上帕馬森起司，散發奢華的菇香氣息。",
            True,
            980,
        )

        self.add_item(
            "甜菜根燉蔬菜塔",
            "層層堆疊的甜菜根、胡蘿蔔與南瓜，搭配香草橄欖油與山羊乳酪，色彩繽紛且清爽，展現法式蔬食美學。",
            True,
            850,
        )

        self.add_item(
            "羊排佐迷迭香紅酒醬",
            "嫩烤羊排帶有淡淡迷迭香香氣，淋上濃縮紅酒醬汁，搭配鼠尾草奶油馬鈴薯泥，醇厚且令人回味。",
            False,
            1_500,
        )

        self.add_item(
            "法式洋蔥湯佐焗起司",
            "慢燉數小時的洋蔥湯，加入紅酒提味，覆蓋一層融化的格呂耶爾起司與酥脆法國麵包，溫暖濃郁的經典滋味。",
            False,
            680,
        )

    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        self.menu_items.append(MenuItem(name, description, vegetarian, price))
        return None
    
    def __iter__(self):
        return iter(self.menu_items)
    
class Waitress:
    def __init__(self, cafe_menu: Menu, diner_menu: Menu):
        self.cafe_menu = cafe_menu
        self.diner_menu = diner_menu
    
    def _print_menu(self, itermenu):
        for menu_item in itermenu:
            print(f"{menu_item.name}, {menu_item.price} -- {menu_item.description}")
    
    def print_menu(self):
        print("MENU\n---\nBREAKFAST")
        print("not implemented")
        print("\nLUNCH")
        self._print_menu(self.diner_menu)
        print("\nDINNER")
        self._print_menu(self.cafe_menu)

    def _is_vegetarian(self, name: str, itermenu: Menu) -> bool:
        for menu_item in itermenu:
            if menu_item.name == name:
                return menu_item.vegetarian
        return False
    
    def is_vegetarian(self, name: str) -> bool:
        if self._is_vegetarian(name, self.cafe_menu):
            return True
        
        if self._is_vegetarian(name, self.diner_menu):
            return True
        
        return False

def menu_test_drive():
    cafe_menu: Menu = CafeMenu()
    diner_menu: Menu = DinerMenu()
    waitress = Waitress(cafe_menu=cafe_menu, diner_menu=diner_menu)
    waitress.print_menu()
    print("\nCustomer asks, is the Hotdog vegetarian?")
    print("Waitress says: ", end="")
    if waitress.is_vegetarian("Hotdog"):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    menu_test_drive()
