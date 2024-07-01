from pizza_factory import Pizza
from pizza_store_factory import PizzaStore
from Chicago_style_pizzas import *

class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, flavor: str) -> Pizza:
        if flavor == "cheese":
            return ChicagoCheesePizza()
        elif flavor == "veggie":
            return ChicagoVeggiePizza()
        elif flavor == "pepperoni":
            return ChicagoPepperoniPizza()
        elif flavor == "clam":
            return ChicagoClamPizza()
        else:
            raise ValueError(f"Unknown pizza flavor: {flavor}")
