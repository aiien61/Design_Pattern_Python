from pizza_factory import Pizza
from pizza_store_factory import PizzaStore
from Chicago_pizza_store import ChicagoPizzaStore
from NewYork_pizza_store import NewYorkPizzaStore


class PizzaTest:
    @staticmethod
    def main(*args) -> None:
        ny_store = NewYorkPizzaStore()
        chicago_store = ChicagoPizzaStore()

        pizza: Pizza = ny_store.order_pizza("cheese")
        print(f"Ethan ordered a {pizza.get_name()}")

        pizza: Pizza = chicago_store.order_pizza("cheese")
        print(f"Joel ordered a {pizza.get_name()}")

        pizza: Pizza = ny_store.order_pizza("pepperoni")
        print(f"Ethan ordered a {pizza.get_name()}")

        pizza: Pizza = chicago_store.order_pizza("pepperoni")
        print(f"Joel ordered a {pizza.get_name()}")

        pizza: Pizza = ny_store.order_pizza("clam")
        print(f"Ethan ordered a {pizza.get_name()}")

        pizza: Pizza = chicago_store.order_pizza("clam")
        print(f"Joel ordered a {pizza.get_name()}")

        pizza: Pizza = ny_store.order_pizza("veggie")
        print(f"Ethan ordered a {pizza.get_name()}")

        pizza: Pizza = chicago_store.order_pizza("veggie")
        print(f"Joel ordered a {pizza.get_name()}")

if __name__ == "__main__":
    PizzaTest.main()
