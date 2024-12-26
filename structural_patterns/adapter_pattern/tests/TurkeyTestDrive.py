from DuckTurkeyAdapter.Adaptee.Duck import Duck, MallardDuck
from DuckTurkeyAdapter.Adaptee.Turkey import Turkey, WildTurkey
from DuckTurkeyAdapter.Adapter.DuckAdpater import DuckAdapter

class TurkeyTestDrive:
    """Test whether duck can successfully be converted to be turkey"""

    @staticmethod
    def main(*args):
        turkey: Turkey = WildTurkey()

        duck: Duck = MallardDuck()
        duck_adapter: DuckAdapter = DuckAdapter(duck)

        print('The duck says...')
        duck_adapter.gobble()
        duck.fly()

        print('The turkey says...')
        TurkeyTestDrive.test_turkey(turkey)

        print('The duck adapter says...')
        TurkeyTestDrive.test_turkey(duck_adapter)
    
    @staticmethod
    def test_turkey(turkey: Turkey):
        turkey.gobble()
        turkey.fly()

if __name__ == '__main__':
    TurkeyTestDrive.main()
