from typing import Iterator, Dict, List
from menu import Menu
from menu_item import MenuItem

class PancakeHouseMenu(Menu):
    menu_items: Dict[str, MenuItem]

    def __init__(self):
        self.menu_items = {}

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

    
    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menu_item: MenuItem = MenuItem(name, description, vegetarian, price)
        self.menu_items[name] = (menu_item)
        return None
    
    def get_menu_items(self) -> List[MenuItem]:
        return self.menu_items.values()
    
    def create_iterator(self) -> Iterator[MenuItem]:
        return iter(self.menu_items.values())