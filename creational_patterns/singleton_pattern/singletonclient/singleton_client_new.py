class Singleton(type):
    __unique_instance: 'Singleton' = None

    def __new__(cls, *args, **kwargs) -> 'Singleton':
        if not cls.__unique_instance:
            cls.__unique_instance = super().__new__(cls, *args, **kwargs)
        return cls.__unique_instance
    
    def get_instance(self):
        return self.__unique_instance
    
    def __repr__(self) -> str:
        return "I am a thread safe singleton"
    
class SingletonClient(metaclass=Singleton):
    pass

def main() -> None:
    client1: SingletonClient = SingletonClient.get_instance()
    print(client1)

    client2: SingletonClient = SingletonClient.get_instance()
    print(client2)

    print(client1 is client2)

if __name__ == '__main__':
    main()