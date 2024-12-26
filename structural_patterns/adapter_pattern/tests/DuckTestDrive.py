from DuckTurkeyAdapter.Adaptee.Duck import Duck, MallardDuck
from DuckTurkeyAdapter.Adaptee.Turkey import Turkey, WildTurkey
from DuckTurkeyAdapter.Adapter.TurkeyAdpater import TurkeyAdapter

class DuckTestDrive:
    """Test whether turkey can successfully be converted to be duck"""
    
    @staticmethod
    def main(*args):
        duck: Duck = MallardDuck()

        turkey: Turkey = WildTurkey()
        turkey_adapter: TurkeyAdapter = TurkeyAdapter(turkey)
        
        print('The turkey says...')
        turkey.gobble()
        turkey.fly()

        print('\nThe duck says...')
        DuckTestDrive.test_duck(duck)

        print('\nThe turkey adapter says...')
        DuckTestDrive.test_duck(turkey_adapter)

    @staticmethod
    def test_duck(duck: Duck) -> None:
        duck.quack()
        duck.fly()

if __name__ == '__main__':
    DuckTestDrive.main()
