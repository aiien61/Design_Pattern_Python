def singleton(class_):
    isinstances = {}

    def get_instance(*args, **kwargs):
        if class_ not in isinstances:
            isinstances[class_] = class_(*args, **kwargs)
        return isinstances[class_]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print('Loading a database...')

if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 == db2)