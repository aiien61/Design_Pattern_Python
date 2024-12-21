from fastfood_eatery.Commands.Order import Order
from fastfood_eatery.Receiver.Cook import Cook


class BurgerOrder(Order):
    def __init__(self, cook: Cook):
        self.cook = cook
        self.order_done: bool = None

    def order_up(self) -> bool:
        self.order_done = self.cook.make_burger()
        return self.order_done
    
    def __repr__(self) -> str:
        return "burger order"
