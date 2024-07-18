class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self) -> None:
        print('Loading a database...')

if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 == db2)