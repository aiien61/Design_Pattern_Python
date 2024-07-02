from abc import ABC, abstractmethod
from typing import List
from ingredient_factory import *

class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> None: raise NotImplementedError

    @abstractmethod
    def create_sauce(self) -> None: raise NotImplementedError

    @abstractmethod
    def create_cheese(self) -> None: raise NotImplementedError

    @abstractmethod
    def create_veggies(self) -> None: raise NotImplementedError

    @abstractmethod
    def create_pepperoni(self) -> None: raise NotImplementedError

    @abstractmethod
    def create_clams(self) -> None: raise NotImplementedError


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()
    
    def create_sauce(self) -> None:
        return PlumTomatoSauce()
    
    def create_cheese(self):
        return MozzarellaCheese()
    
    def create_veggies(self):
        return [BlackOlives(), Spinach(), Aubergine()]
    
    def create_pepperoni(self):
        return SlicedPepperoni()
    
    def create_clams(self):
        return FrozenClams()


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()
    
    def create_sauce(self) -> None:
        return MarinaraSauce()
    
    def create_cheese(self):
        return ReggianoCheese()
    
    def create_veggies(self):
        return [Garlic(), Onions(), Mushrooms(), RedPeppers()]
    
    def create_pepperoni(self):
        return SlicedPepperoni()
    
    def create_clams(self) -> None:
        return FreshClams()


class Pizza:
    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        self.ingredient_factory: PizzaIngredientFactory = ingredient_factory
        self.name: str = None
        self.dough: Dough = None
        self.sauce: Sauce = None
        self.cheese: Cheese = None
        self.veggies: List[Veggies] = []
        self.pepperoni: Pepperoni = None
        self.clams: Clams = None
    
    @abstractmethod
    def prepare(self): raise NotImplementedError

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    # @property
    # def name(self):
    #     return self.name
    
    # @name.setter
    # def name(self, name):
    #     self.name = name

    def __str__(self):
        result = []
        result.append(f"《{self.name}》")
        result.append(f"---- ingredents ----")
        if self.dough:
            result.append(self.dough)
        if self.sauce:
            result.append(self.sauce)
        if self.cheese:
            result.append(self.cheese)
        if self.veggies:
            result.append(", ".join(map(str, self.veggies)))
        if self.pepperoni:
            result.append(self.pepperoni)
        if self.clams:
            result.append(self.clams)
        return "\n".join(map(str, result)) + "\n"
    
class CheesePizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clams = self.ingredient_factory.create_clams()

class VeggiePizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()

class PepperoniPizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()
        self.pepperoni = self.ingredient_factory.create_pepperoni()
