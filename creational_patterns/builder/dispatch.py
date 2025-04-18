"""
範例情境：供應鏈管理中的「建立訂單派送指令」

建立一份複雜的「訂單派送指令」
指令中包含：訂單編號、倉庫地點、物流方式、貨運優先順序等
每種案例可能會建立不同內容但類似結構的指令


Builder模式中的角色
Builder         | 定義每個建構步驟的介面
ConcreteBuilder | 實作建構步驟，組裝具體物件
Director        | 負責按順序呼叫建構步驟
Product         | 最終組裝出來的複雜對象
"""
from typing import List
from enum import Enum, auto

class Level(Enum):
    EXPRESS = auto()
    REGULAR = auto()

# Product: 最終指令
class DispatchOrder:
    def __init__(self):
        self.parts: List[str] = []

    def add_part(self, info):
        self.parts.append(info)

    def show(self):
        return "\n".join(self.parts)

# Builder: 建構指令的步驟
class OrderBuilder:
    def reset(self): pass
    def add_order_id(self, order_id: str): pass
    def set_warehouse(self, location: str): pass
    def choose_logistics(self, method: str): pass
    def set_priority(self, level: Level): pass
    def get_result(self): pass

# ConcreteBuilder: 實作細節
class ConcreteOrderBuilder(OrderBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.order = DispatchOrder()

    def add_order_id(self, order_id: str) -> None:
        self.order.add_part(f"訂單編號: {order_id}")

    def set_warehouse(self, location: str) -> None:
        self.order.add_part(f"出貨倉庫: {location}")
    
    def choose_logistics(self, method: str) -> None:
        self.order.add_part(f"物流方式: {method}")
    
    def set_priority(self, level: Level) -> None:
        self.order.add_part(f"優先順序: {level}")

    def get_result(self) ->DispatchOrder:
        return self.order

# Director: 控制建構流程
class DispatchDirector:
    def __init__(self, builder: OrderBuilder):
        self.builder = builder
    
    def construct_express_order(self, order_id: str) -> DispatchOrder:
        self.builder.reset()
        self.builder.add_order_id(order_id)
        self.builder.set_warehouse("台中倉庫")
        self.builder.choose_logistics("黑貓宅急便")
        self.builder.set_priority(Level.EXPRESS)
        return self.builder.get_result()
    
    def construct_regular_order(self, order_id: str) -> DispatchOrder:
        self.builder.reset()
        self.builder.add_order_id(order_id)
        self.builder.set_warehouse("高雄倉庫")
        self.builder.choose_logistics("新竹物流")
        self.builder.set_priority(Level.REGULAR)
        return self.builder.get_result()

if __name__ == "__main__":
    builder = ConcreteOrderBuilder()
    director = DispatchDirector(builder)

    order1 = director.construct_express_order("ORD-001")
    order2 = director.construct_regular_order("ORD-002")

    print("🚚 派送指令 A：")
    print(order1.show())

    print("\n🚛 派送指令 B：")
    print(order2.show())
