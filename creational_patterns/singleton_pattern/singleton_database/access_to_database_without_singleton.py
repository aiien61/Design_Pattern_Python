import random
class Database:
    _instance: 'Database' = None

    def __init__(self):
        self.id = random.randint(1, 101)
        print(f'Loading a database... id: {self.id}')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 == db2)