from pizza import Pizza
from pizza_styles import *

class SimplePizzaFactory:
    def create_pizza(self, flavor: str) -> Pizza:
        pizza: Pizza = None
        if flavor == "cheese":
            pizza = CheesePizza()
        elif flavor == "pepperoni":
            pizza = PepperoniPizza()
        elif flavor == "clam":
            pizza = ClamPizza()
        elif flavor == "veggie":
            pizza = VeggiePizza()
        else:
            raise ValueError(f"Unknown pizza flavor: {flavor}")
        return pizza