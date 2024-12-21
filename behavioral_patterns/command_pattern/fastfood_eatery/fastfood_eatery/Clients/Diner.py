from fastfood_eatery.Receiver.Cook import Cook
from fastfood_eatery.Commands.BurgerOrder import BurgerOrder
from fastfood_eatery.Commands.SaladOrder import SaladOrder
from fastfood_eatery.Invokers.Waiter import Waiter
from fastfood_eatery.Clients.Customer import Customer

class Diner:
    @staticmethod
    def main(*args) -> None:
        cook: Cook = Cook()
        waiter: Waiter = Waiter()
        customer: Customer = Customer(waiter)
        customer.create_order(BurgerOrder(cook), SaladOrder(cook))
        customer.place_order()

if __name__ == '__main__':
    Diner.main()
