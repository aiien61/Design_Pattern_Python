from fastfood_eatery.Commands.Order import Order

class Waiter:
    def __init__(self):
        self.order: Order = None
        self.order_taken: bool = None
    
    def take_order(self, order: Order) -> bool:
        self.order = order
        self.order_taken = self.order.order_up()
        return self.order_taken