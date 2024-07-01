from pizza_factory import Pizza

class ChicagoStylePizza(Pizza):
    def __init__(self) -> None:
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = ["Shredded Mozzarella Cheese"]

    def cut(self):
        print("Cutting the pizza into square slices")
        

class ChicagoCheesePizza(ChicagoStylePizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"


class ChicagoVeggiePizza(ChicagoStylePizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Deep Dish Veggie Pizza"
        self.toppings.append("Black Olives")
        self.toppings.append("Spinach")
        self.toppings.append("Aubergine")

class ChicagoPepperoniPizza(ChicagoStylePizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Deep Dish Veggie Pizza"
        self.toppings.append("Black Olives")
        self.toppings.append("Spinach")
        self.toppings.append("Aubergine")
        self.toppings.append("Sliced Pepperoni")

class ChicagoClamPizza(ChicagoStylePizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Deep Dish Veggie Pizza"
        self.toppings.append("Fresh Clams from Chesapeake Bay")
