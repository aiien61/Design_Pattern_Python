from pizza_factory import Pizza
from pizza_store_factory import PizzaStore
from NewYork_style_pizzas import *

class NewYorkPizzaStore(PizzaStore):
    def create_pizza(self, flavor: str) -> Pizza:
        if flavor == "cheese":
            return NewYorkCheesePizza()
        elif flavor == "veggie":
            return NewYorkVeggiePizza()
        elif flavor == "pepperoni":
            return NewYorkPepperoniPizza()
        elif flavor == "clam":
            return NewYorkClamPizza()
        else:
            raise ValueError(f"Unknown pizza flavor: {flavor}")
