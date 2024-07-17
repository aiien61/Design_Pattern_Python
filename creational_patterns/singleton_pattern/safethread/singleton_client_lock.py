from threading import Lock, Thread

class SingletonClient:
    __unique_instance: 'SingletonClient' = None
    __lock: Lock = Lock()

    def __init__(self):
        self.order_amount: int = 0

    @staticmethod
    def get_instance() -> 'SingletonClient':
        with SingletonClient.__lock:
            if SingletonClient.__unique_instance is None:
                SingletonClient.__unique_instance = SingletonClient()
        return SingletonClient.__unique_instance
    
    def place_order(self, amount: int) -> None:
        self.order_amount += amount

    def cancel_order(self, amount: int) -> None:
        self.order_amount -= amount

    def get_order_amount(self) -> int:
        return self.order_amount
    

def place_order(amount: int):
    client: SingletonClient = SingletonClient.get_instance()
    client.place_order(amount)

def cancel_order(amount: int):
    client: SingletonClient = SingletonClient.get_instance()
    client.cancel_order(amount)


def main() -> None:
    client_thread1: Thread = Thread(target=place_order, args=(10,))
    client_thread1.start()

    client_thread2: Thread = Thread(target=cancel_order, args=(10,))
    client_thread2.start()

    client_thread1.join()
    client_thread2.join()

    order_amount: int = SingletonClient.get_instance().get_order_amount()
    print(f'Order amount: {order_amount}')


if __name__ == '__main__':
    main()