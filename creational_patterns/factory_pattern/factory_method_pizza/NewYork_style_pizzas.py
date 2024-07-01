from pizza_factory import Pizza

class NewYorkStylePizza(Pizza):
    def __init__(self):
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Reggiano Cheese"]


class NewYorkCheesePizza(NewYorkStylePizza):
    def __init__(self):
        super().__init__()
        self.name = "NewYork Style Sauce and Cheese Pizza"


class NewYorkVeggiePizza(NewYorkStylePizza):
    def __init__(self):
        super().__init__()
        self.name = "NewYork Style Veggie Pizza"
        self.toppings.append("Garlic")
        self.toppings.append("Mushrooms")
        self.toppings.append("Onions")
        self.toppings.append("Red Peppers")


class NewYorkClamPizza(NewYorkStylePizza):
    def __init__(self):
        super().__init__()
        self.name = "NewYork Style Clam Pizza"
        self.toppings.append("Fresh Clams from Long Island Sound")


class NewYorkPepperoniPizza(NewYorkStylePizza):
    def __init__(self):
        super().__init__()
        self.name = "NewYork Style Pepperoni Pizza"
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Garlic")
        self.toppings.append("Onions")
        self.toppings.append("Mushrooms")
        self.toppings.append("Red Peppers")
