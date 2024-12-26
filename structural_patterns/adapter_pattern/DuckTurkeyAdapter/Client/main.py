from DuckTurkeyAdapter.Adaptee.Duck import Duck, MallardDuck
from DuckTurkeyAdapter.Adaptee.Turkey import Turkey, WildTurkey
from DuckTurkeyAdapter.Adapter.DuckAdpater import DuckAdapter
from DuckTurkeyAdapter.Adapter.TurkeyAdpater import TurkeyAdapter

def turkey_to_duck():
    duck: Duck = MallardDuck()

    turkey: Turkey = WildTurkey()
    turkey_adapter: TurkeyAdapter = TurkeyAdapter(turkey)

    print('The turkey says...')
    turkey.gobble()
    turkey.fly()

def duck_to_turkey():
    turkey: Turkey = WildTurkey()

    duck: Duck = MallardDuck()
    duck_adapter: DuckAdapter = DuckAdapter(turkey)

    print('The duck says...')
    duck.quack()
    duck.fly()

if __name__ == '__main__':
    turkey_to_duck()
    duck_to_turkey()
