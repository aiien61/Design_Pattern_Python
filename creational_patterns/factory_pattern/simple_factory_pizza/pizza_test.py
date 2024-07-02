from pizza import Pizza
from pizza_store import PizzaStore
from simple_pizza_factory import SimplePizzaFactory

class PizzaTest:
    @staticmethod
    def main(*args) -> None:
        factory: SimplePizzaFactory = SimplePizzaFactory()
        store: PizzaStore = PizzaStore(factory)

        pizza: Pizza = store.order_pizza("cheese")
        print(f"We ordered a {pizza.get_name()}")
        print(pizza.to_string())

        pizza = store.order_pizza("veggie")
        print(f"We ordered a {pizza.get_name()}")
        print(pizza.to_string())

if __name__ == "__main__":
    PizzaTest.main()
