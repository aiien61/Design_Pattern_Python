from pizza import Pizza

class CheesePizza(Pizza):
    def __init__(self):
        self.name= "Cheese Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings = ["Fresh Mozzarella Cheese", "Parmesan Cheese"]


class ClamPizza(Pizza):
    def __init__(self):
        self.name = "Clam Pizza"
        self.dough = "Thick Crust"
        self.sauce = "White Garlic Sauce"
        self.toppings = ["Clams", "Grated Parmesan Cheese"]


class PepperoniPizza(Pizza):
    def __init__(self):
        self.name = "Pepperoni Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Sliced Pepperoni", "Sliced Onion", "Grated Parmesan Cheese"]

class VeggiePizza(Pizza):
    def __init__(self):
        self.name = "Veggie Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara Sauce"
        self.toppings = []
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Diced Onion")
        self.toppings.append("Grated Parmesan Cheese")
        self.toppings.append("Sliced mushrooms")
        self.toppings.append("Sliced Red Peppers")
        self.toppings.append("Sliced Black Olives")
