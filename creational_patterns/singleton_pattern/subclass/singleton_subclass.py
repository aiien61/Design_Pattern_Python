from threading import Lock

class Singleton:
    __unique_instance: 'Singleton' = None
    __lock: Lock = Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_instance() -> 'Singleton':
        with Singleton.__lock:
            if Singleton.__unique_instance is None:
                Singleton.__unique_instance = Singleton()
        return Singleton.__unique_instance


class HotterSingleton(Singleton):
    pass

class CoolerSingleton(Singleton):
    pass

class SingletonTestDrive:
    @staticmethod
    def main() -> None:
        s1: Singleton = HotterSingleton.get_instance()
        s2: Singleton = CoolerSingleton.get_instance()

        print(s1)
        print(s2)

        print(s1 is s2)

if __name__ == '__main__':
    SingletonTestDrive.main()