from pizza_store_factory import *

def pizza_test():
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()
    pizza: Pizza = None
    
    pizza = ny_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza}")
    pizza = chicago_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza}")
    
    pizza = ny_store.order_pizza("clam")
    print(f"Joel ordered a {pizza}")
    pizza = chicago_store.order_pizza("clam")
    print(f"Joel ordered a {pizza}")

    pizza = ny_store.order_pizza("pepperoni")
    print(f"Joel ordered a {pizza}")
    pizza = chicago_store.order_pizza("pepperoni")
    print(f"Joel ordered a {pizza}")

    pizza = ny_store.order_pizza("veggie")
    print(f"Joel ordered a {pizza}")
    pizza = chicago_store.order_pizza("veggie")
    print(f"Joel ordered a {pizza}")

if __name__ == "__main__":
    pizza_test()