from abc import ABC

class Cheese(ABC):
    def __str__(self): raise NotImplementedError

class MozzarellaCheese(Cheese):
    def __str__(self): return "Shredded Mozzarella"

class ParmesanCheese(Cheese):
    def __str__(self): return "Shredded Parmesan"

class ReggianoCheese(Cheese):
    def __str__(self): return "Reggiano Cheese"

class Dough(ABC):
    def __str__(self): raise NotImplementedError

class ThinCrustDough(Dough):
    def __str__(self): return "Thin Crust Dough"

class ThickCrustDough(Dough):
    def __str__(self): return "ThickCrust Style Extra Crust Dough"

class Clams(ABC):
    def __str__(self): raise NotImplementedError

class FreshClams(Clams):
    def __str__(self): return "Fresh Clams from Long Island Sound"

class FrozenClams(Clams):
    def __str__(self): return "Frozen Clams from Chesapeake Bay"

class Sauce(ABC):
    def __str__(self): raise NotImplementedError

class MarinaraSauce(Sauce):
    def __str__(self): return "Marinara Sauce"

class PlumTomatoSauce(Sauce):
    def __str__(self): return "Tomato Sauce with Plum Tomatoes"


class Veggies(ABC):
    def __str__(self): raise NotImplementedError


class Spinach(Veggies):
    def __str__(self): return "Spinach"


class BlackOlives(Veggies):
    def __str__(self): return "Black Olives"


class Aubergine(Veggies):
    def __str__(self): return "Aubergine"


class Garlic(Veggies):
    def __str__(self): return "Garlic"


class Mushrooms(Veggies):
    def __str__(self): return "Mushrooms"


class Onions(Veggies):
    def __str__(self): return "Onions"


class RedPeppers(Veggies):
    def __str__(self): return "Red Peppers"


class Pepperoni(ABC):
    def __str__(self): raise NotImplementedError


class SlicedPepperoni(Pepperoni):
    def __str__(self): return "Sliced Pepperoni"
