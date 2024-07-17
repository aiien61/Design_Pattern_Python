from enum import Enum, auto

class Singleton(Enum):
    UNIQUE_INSTANCE = auto()

    def __str__(self) -> str:
        return 'I am a thread safe singleton'
    
class SingletonClient:
    @staticmethod
    def main() -> None:
        client1: Singleton = Singleton.UNIQUE_INSTANCE
        print(client1)

        client2: Singleton = Singleton.UNIQUE_INSTANCE
        print(client2)

        print(client1 is client2)

if __name__ == '__main__':
    SingletonClient.main()