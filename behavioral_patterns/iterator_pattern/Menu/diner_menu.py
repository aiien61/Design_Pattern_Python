from typing import Final, Iterator, List
from menu import Menu
from menu_item import MenuItem

class DinerMenu(Menu):
    MAX_ITEMS: Final[int] = 6
    number_of_items: int = 0
    menu_items: List[MenuItem]

    def __init__(self):
        self.menu_items = []

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

    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menu_item: MenuItem = MenuItem(name, description, vegetarian, price)
        if self.number_of_items >= self.MAX_ITEMS:
            print("Sorry, menu is full! Can't add item to menu")
        else:
            self.menu_items.append(menu_item)
            self.number_of_items += 1
    
    def get_menu_items(self) -> List[MenuItem]:
        return self.menu_items
    
    def create_iterator(self) -> Iterator[MenuItem]:
        return iter(self.menu_items)
