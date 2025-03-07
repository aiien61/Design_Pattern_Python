from typing import Iterator, Iterable, List, Dict, Optional, Final, Any
from abc import ABC, abstractmethod
from rich import print

class MenuItem:
    def __init__(self, name: str, description: str, veggie: bool, price: int):
        self.name = name
        self.description = description
        self.veggie = veggie
        self.price = price

    def __repr__(self):
        return f"{self.name}, {self.price} -- {self.description}\n"


class Menu(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator[MenuItem]:
        raise NotImplementedError


class DinerMenuIterator(Iterator[MenuItem]):
    def __init__(self, menu_list: List[MenuItem]):
        self.menu_list = menu_list
        self.position: int = 0

    def __next__(self) -> MenuItem:
        if self.position >= len(self.menu_list):
            raise StopIteration
        menu_item: MenuItem = self.menu_list[self.position]
        self.position += 1
        return menu_item
    
    def __iter__(self):
        return self


class DinerMenu(Menu):
    def __init__(self):
        self.menu_items: List[MenuItem] = []

        self.add_item(
            "義大利野菇燉飯",
            "使用新鮮松露菇、牛肝菌與義大利米，搭配濃郁奶油與帕馬森起司，口感滑順濃香，帶有淡淡的菇類清甜。",
            True,
            280
        )

        self.add_item(
            "台式滷肉飯",
            "肥瘦適中的豬五花肉慢燉數小時，搭配濃郁醬汁與白飯，撒上些許蔥花與滷蛋，簡單卻滿足的經典台灣滋味。",
            False,
            120
        )

        self.add_item(
            "日式炸豬排咖喱飯",
            "酥脆的炸豬排鋪在熱騰騰的白飯上，淋上濃郁的日式咖喱醬，搭配醃漬小菜，口感豐富且開胃。",
            False,
            220
        )

        self.add_item(
            "地中海蔬菜沙拉",
            "新鮮生菜、番茄、小黃瓜、橄欖與羊奶起司，淋上橄欖油與檸檬汁，清爽健康，適合輕食愛好者。",
            True,
            180
        )

        self.add_item(
            "麻婆豆腐拌飯",
            "嫩滑豆腐搭配麻辣醬汁與牛絞肉，濃郁的川味辣香覆蓋在白飯上，讓人忍不住一口接一口。",
            False,
            150
        )

        self.add_item(
            "椰香南瓜濃湯配麵包",
            "南瓜慢熬成濃湯，加入椰奶提升香氣，搭配剛出爐的蒜香麵包，溫暖又滿足的選擇。",
            True,
            200
        )

    def add_item(self, name: str, description: str, veggie: bool, price: int) -> None:
        self.menu_items.append(MenuItem(name, description, veggie, price))
        return None
    
    def create_iterator(self) -> Iterator[MenuItem]:
        return DinerMenuIterator(self.menu_items)
    

class PancakeHouseIterator(Iterator[MenuItem]):
    def __init__(self, items: Dict[str, MenuItem]):
        self.items: List[MenuItem] = list(items.values())
        self.position: int = 0

    def __iter__(self) -> bool:
        return self

    def __next__(self):
        if self.position >= len(self.items):
            raise StopIteration
        menu_item: MenuItem = self.items[self.position]
        self.position += 1
        return menu_item


class PancakeHouseMenu(Menu):
    def __init__(self):
        self.menu_items: Dict[str, MenuItem] = {}

        self.add_item(
            "經典藍莓鬆餅",
            "蓬鬆的原味鬆餅，搭配新鮮藍莓與楓糖漿，撒上少許糖粉，簡單卻充滿果香的甜美滋味。",
            True,
            180
        )

        self.add_item(
            "焦糖香蕉培根鬆餅",
            "熱氣蒸騰的鬆餅上鋪滿香煎培根與焦糖化的香蕉片，淋上濃郁焦糖醬，鹹甜交織的絕妙享受。",
            False,
            220
        )

        self.add_item(
            "草莓鮮奶油鬆餅",
            "柔軟鬆餅搭配手打鮮奶油與新鮮草莓，輕盈酸甜，適合下午茶時光的小確幸。",
            True,
            200
        )

        self.add_item(
            "巧克力熔岩鬆餅",
            "外酥內軟的巧克力鬆餅，切開後流出溫熱濃郁的巧克力醬，搭配一球香草冰淇淋，甜點控的最愛。",
            True,
            230
        )

        self.add_item(
            "抹茶紅豆鬆餅",
            "抹茶風味的鬆餅，搭配日式甜紅豆與一抹鮮奶油，撒上抹茶粉，帶有東方雅致的清新甜感。",
            True,
            210
        )

    def add_item(self, name: str, description: str, veggie: bool, price: int) -> None:
        self.menu_items[name] = MenuItem(name, description, veggie, price)
        return None
    
    def create_iterator(self):
        return PancakeHouseIterator(self.menu_items)


class Waitress:
    def __init__(self, menus: List[Menu]):
        self.menus = menus

    def print_menu(self) -> None:
        print('MENU')
        for menu in self.menus:
            self._print_menu(menu.create_iterator())

    def _print_menu(self, menu_iterator: Iterator[MenuItem]) -> None:
        for item in menu_iterator:
            print(item)

    def print_vegetarian_menu(self) -> None:
        print('VEGETARIAN MENU')
        for menu in self.menus:
            self._print_vegetarian(menu.create_iterator())

    def _print_vegetarian(self, menu_iterator: Iterator[MenuItem]) -> None:
        for item in menu_iterator:
            if item.veggie:
                print(item)

if __name__ == "__main__":
    menus: List[Menu] = [PancakeHouseMenu(), DinerMenu()]
    waitress = Waitress(menus)
    waitress.print_menu()
    print("\n--------------------------\n")
    waitress.print_vegetarian_menu()
