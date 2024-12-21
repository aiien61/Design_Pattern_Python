from fastfood_eatery.Commands.Order import Order
from fastfood_eatery.Invokers.Waiter import Waiter
from typing import List

# TODO: Macro
class Customer:
    waiter: Waiter
    order: Order
    order_placed: bool

    def __init__(self, waiter: Waiter):
        self.waiter = waiter
        self.order = []
        self.order_placed = None
    
    def create_order(self, *item_orders: List[Order]) -> None:
        for item in item_orders:
            self.order.append(item)
            print(f'Add {item} in order')

    def place_order(self) -> bool:
        for item_order in self.order:
            self.order_placed = self.waiter.take_order(item_order)
            if not self.order_placed:
                print(f"{item_order} fails")

        return self.order_placed
