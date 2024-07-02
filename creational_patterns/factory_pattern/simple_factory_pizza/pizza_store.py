from pizza import Pizza
from simple_pizza_factory import SimplePizzaFactory

class PizzaStore:
    factory: SimplePizzaFactory

    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    def order_pizza(self, flavor: str) -> Pizza:
        pizza: Pizza = self.factory.create_pizza(flavor)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
