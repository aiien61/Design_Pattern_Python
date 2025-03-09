from __future__ import annotations
from typing import List

class MenuComponent:
    def add(self, menu_component) -> None:
        raise NotImplementedError
    
    def remove(self, menu_component) -> None:
        raise NotImplementedError
    
    def get_child(self, i: int) -> "MenuComponent":
        raise NotImplementedError

    def print(self):
        raise NotImplementedError
    
class MenuItem(MenuComponent):
    def __init__(self, name: str, description: str, veggie: bool, price: int):
        self.name = name
        self.description = description
        self.veggie = veggie
        self.price = price
    
    def print(self) -> None:
        print(f" {self.name} {'(v)' if self.veggie else ''}, {self.price}")
        print(f"     -- {self.description}\n")

class Menu(MenuComponent):
    def __init__(self, name: str, description: str):
        self.menu_components: List[MenuComponent] = []
        self.name = name
        self.description = description

    def add(self, menu_component: MenuComponent):
        self.menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponent):
        self.menu_components.remove(menu_component)

    def get_child(self, i: int) -> MenuComponent:
        return self.menu_components[i]
    
    def print(self):
        print(f"\n{self.name}, {self.description}")
        print('--------------------')

        for menu_component in self.menu_components:
            menu_component.print()
    
class Waitress:
    def __init__(self, all_menus: MenuComponent):
        self.all_menus = all_menus
    
    def print_menu(self):
        self.all_menus.print()

def menu_test_drive():
    # Creating main menu categories
    cafe_menu = Menu('Cafe Menu', 'For Lunch')
    diner_menu = Menu('Diner Menu', 'For Dinner')
    all_menus: MenuComponent = Menu('all menus', 'all menus')

    # Adding menus to the main menu
    all_menus.add(cafe_menu)
    all_menus.add(diner_menu)

    # Adding menu items to Cafe Menu
    cafe_menu.add(
        MenuItem("素食黑豆漢堡", 
                 "以黑豆與蔬菜製成的素肉餅，搭配酪梨醬、生菜與番茄，清爽又營養。", 
                 True, 
                 150)
    )

    cafe_menu.add(
        MenuItem("起司薯條", 
                 "金黃酥脆的薯條，淋上濃濃的溫熱起司醬，簡單卻令人滿足的速食經典。", 
                 True, 
                 120)
    )

    cafe_menu.add(
        MenuItem("BBQ豬肋排套餐", 
                 "慢烤至軟嫩的豬肋排，刷上濃郁的燒烤醬，搭配薯條與玉米沙拉，份量十足的美式風情", 
                 False, 
                 280)
    )

    diner_menu.add(
        MenuItem("法式鴨胸佐橙酒醬",
                 "外皮酥脆、內裡粉嫩的鴨胸，搭配濃郁橙酒醬汁與焦糖橙片，佐以百里香烤小土豆，酸甜與肉香完美平衡。",
                 False,
                 1_200,)
    )
    
    # Adding menu items to Diner Menu
    diner_menu.add(
        MenuItem("松露奶油蘑菇燉飯",
                 "使用義大利阿博利歐米與新鮮松露，慢煮於濃郁奶油與白酒中，撒上帕馬森起司，散發奢華的菇香氣息。",
                 True,
                 980,)
    )

    diner_menu.add(
        MenuItem("甜菜根燉蔬菜塔",
                 "層層堆疊的甜菜根、胡蘿蔔與南瓜，搭配香草橄欖油與山羊乳酪，色彩繽紛且清爽，展現法式蔬食美學。",
                 True,
                 850,)
    )

    diner_menu.add(
        MenuItem("羊排佐迷迭香紅酒醬",
                 "嫩烤羊排帶有淡淡迷迭香香氣，淋上濃縮紅酒醬汁，搭配鼠尾草奶油馬鈴薯泥，醇厚且令人回味。",
                 False,
                 1_500,)
    )

    diner_menu.add(
        MenuItem("法式洋蔥湯佐焗起司",
                 "慢燉數小時的洋蔥湯，加入紅酒提味，覆蓋一層融化的格呂耶爾起司與酥脆法國麵包，溫暖濃郁的經典滋味。",
                 False,
                 680,)
    )

    # Print the menu using the Waitress
    waitress = Waitress(all_menus)
    waitress.print_menu()

if __name__ == "__main__":
    menu_test_drive()