from DuckTurkeyAdapter.Adaptee.Duck import Duck, MallardDuck
from DuckTurkeyAdapter.Adaptee.Turkey import Turkey, WildTurkey
from DuckTurkeyAdapter.Adaptee.Drone import Drone, SuperDrone
from DuckTurkeyAdapter.Adapter.DuckAdpater import DuckAdapter
from DuckTurkeyAdapter.Adapter.TurkeyAdpater import TurkeyAdapter
from DuckTurkeyAdapter.Adapter.DroneAdapter import DroneAdapter

def turkey_to_duck():
    turkey: Turkey = WildTurkey()
    turkey_adapter: TurkeyAdapter = TurkeyAdapter(turkey)
    
    drone: Drone = SuperDrone()
    drone_adapter: DroneAdapter = DroneAdapter(drone)

    print('The turkey says...')
    turkey.gobble()
    turkey.fly()

    print('\nThe turkey adapter says...')
    turkey_adapter.quack()
    turkey_adapter.fly()

    print('\nThe drone adapter says...')
    drone_adapter.quack()
    drone_adapter.fly()


def duck_to_turkey():
    turkey: Turkey = WildTurkey()

    duck: Duck = MallardDuck()
    duck_adapter: DuckAdapter = DuckAdapter(duck)

    for i in range(10):
        print('The duck adapter says...')
        duck_adapter.gobble()
        duck_adapter.fly()

if __name__ == '__main__':
    turkey_to_duck()
    duck_to_turkey()
