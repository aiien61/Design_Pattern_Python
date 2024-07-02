from abc import ABC, abstractmethod
from pizza_factory import *

class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, flavor: str): raise NotImplementedError

    def order_pizza(self, flavor: str):
        pizza: Pizza = self.create_pizza(flavor)
        print(f"--- Making a {pizza.name} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    
class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, flavor: str):
        pizza: Pizza = None
        ingredient_factory: PizzaIngredientFactory = ChicagoPizzaIngredientFactory()
        if flavor == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "Chicago Style Cheese Pizza"
        elif flavor == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.name = "Chicago Style Veggie Pizza"
        elif flavor == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "Chicago Style Clam Pizza"
        elif flavor == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = "Chicago Style Pepperoni Pizza"
        return pizza
    
class NYPizzaStore(PizzaStore):
    def create_pizza(self, flavor: str):
        pizza: Pizza = None
        ingredient_factory: PizzaIngredientFactory = NYPizzaIngredientFactory()
        if flavor == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "New York Style Cheese Pizza"
        elif flavor == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.name = "New York Style Veggie Pizza"
        elif flavor == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "New York Style Clam Pizza"
        elif flavor == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = "New York Style Pepperoni Pizza"
        return pizza
