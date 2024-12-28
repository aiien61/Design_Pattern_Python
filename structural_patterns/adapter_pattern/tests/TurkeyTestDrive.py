from DuckTurkeyAdapter.Adaptee.Duck import Duck, MallardDuck
from DuckTurkeyAdapter.Adaptee.Turkey import Turkey, WildTurkey
from DuckTurkeyAdapter.Adapter.DuckAdpater import DuckAdapter

class TurkeyTestDrive:
    """Test whether instances have turkey-related behaviours"""

    @staticmethod
    def main(*args):
        duck: Duck = MallardDuck()
        duck_adapter: DuckAdapter = DuckAdapter(duck)

        for i in range(10):
            print('\nThe duck adapter says...')
            duck_adapter.gobble()
            duck_adapter.fly()

if __name__ == '__main__':
    TurkeyTestDrive.main()
