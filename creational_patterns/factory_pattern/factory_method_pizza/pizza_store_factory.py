from abc import ABC, abstractmethod
from pizza_factory import Pizza

class PizzaStore(ABC):

    @abstractmethod
    def create_pizza(self, flavor: str) -> Pizza: raise NotImplementedError

    def order_pizza(self, flavor: str) -> Pizza:
        pizza: Pizza = self.create_pizza(flavor)
        print(f"--- Making a {pizza.name} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
