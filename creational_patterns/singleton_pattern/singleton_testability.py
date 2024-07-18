import unittest

class Singleton(type):
    _isntances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._isntances:
            cls._isntances[cls] = super().__call__(*args, **kwargs)
        return cls._isntances[cls]
    
class CityDatabase(metaclass=Singleton):
    def __init__(self, db_uri: str):
        self.population: dict = {}
        with open(db_uri, 'r') as data:
            lines = data.readlines()
            for i in range(0, len(lines), 2):
                self.population[lines[i].strip()] = int(lines[i + 1].strip())

# Not recommended for testing
class SingletonRecordFinder:
    def total_population(self, db_uri: str, *cities):
        result: int = 0
        for city in cities:
            result += CityDatabase(db_uri).population[city]
        return result

class ConfigurableRecordFinder:
    def __init__(self, db: CityDatabase):
        self.db: CityDatabase = db

    def total_population(self, *cities):
        result: int = 0
        for city in cities:
            result += self.db.population[city]
        return result
    
class DummyCityDatabase:
    population = {
        'alpha': 1,
        'beta': 2,
        'gamma': 3
    }

    def get_population(self, name: str):
        return self.population[name]

class SingletonTest(unittest.TestCase):
    def test_is_signleton(self):
        db1 = CityDatabase('test_db.txt')
        db2 = CityDatabase('test_db.txt')
        expected: bool = True
        actual: bool = db1 is db2
        self.assertEqual(expected, actual)

    def test_singleton_total_population_when_alpha_and_beta_cities(self):
        ddb: DummyCityDatabase = DummyCityDatabase()
        crf = ConfigurableRecordFinder(ddb)
        expected: int = ddb.get_population('alpha') + ddb.get_population('beta')
        actual: int = crf.total_population('alpha', 'beta')
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
