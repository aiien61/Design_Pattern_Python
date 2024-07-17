class Singleton:
    __unique_instance: 'Singleton' = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance() -> 'Singleton':
        if Singleton.__unique_instance is None:
            Singleton.__unique_instance = Singleton()
        return Singleton.__unique_instance
    
    def __str__(self) -> str:
        return 'I am the client instance'
    
class SingletonClient:
    @staticmethod
    def main() -> None:
        client1: Singleton = Singleton.get_instance()
        print(client1)

        client2: Singleton = Singleton.get_instance()
        print(client2)

        print(client1 is client2)

if __name__ == '__main__':
    SingletonClient.main()