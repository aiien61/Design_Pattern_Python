def singletonperson(cls):
    print("decorator called")
    def inner(*args, **kwargs):
        print("inner called")
        if hasattr(cls, '__instance'):
            print("There already exists an instance")
            return getattr(cls, '__instance')
        obj = cls(*args, **kwargs)
        setattr(cls, '__instance', obj)
        print("There doesn't exist an instance. A new instace is created.")
        return obj
    return inner


@singletonperson
class Person:
    pass


def singletoncar(cls):
    _instance: dict = {}

    def inner(*args, **kwargs):
        if cls not in _instance:
            obj = cls(*args, **kwargs)
            _instance[cls] = obj
        return _instance[cls]
    return inner

@singletoncar
class Car:
    pass


class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            obj = super().__call__(*args, **kwargs)
            setattr(cls, '_instance', obj)
        return getattr(cls, '_instance')
    
class iPhone(metaclass=SingletonMeta):
    pass


class SingletonTestDrive:
    @staticmethod
    def main():
        p1 = Person()
        p2 = Person()
        print(p1 is p2)

        c1 = Car()
        c2 = Car()
        print(c1 is c2)

        i15 = iPhone()
        i16 = iPhone()
        print(i15 is i15)

if __name__ == '__main__':
    SingletonTestDrive.main()