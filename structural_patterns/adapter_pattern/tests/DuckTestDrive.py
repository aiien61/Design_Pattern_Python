from DuckTurkeyAdapter.Adaptee.Duck import Duck, MallardDuck
from DuckTurkeyAdapter.Adaptee.Turkey import Turkey, WildTurkey
from DuckTurkeyAdapter.Adaptee.Drone import Drone, SuperDrone
from DuckTurkeyAdapter.Adapter.TurkeyAdpater import TurkeyAdapter
from DuckTurkeyAdapter.Adapter.DroneAdapter import DroneAdapter

class DuckTestDrive:
    """Test whether instances have duck-related behaviours"""

    @staticmethod
    def main(*args):
        turkey: Turkey = WildTurkey()
        turkey_adapter: TurkeyAdapter = TurkeyAdapter(turkey)

        drone: Drone = SuperDrone()
        drone_adapter: DroneAdapter = DroneAdapter(drone)
        
        print('The turkey says...')
        turkey.gobble()
        turkey.fly()

        print('\nThe turkey adapter says...')
        DuckTestDrive.test_duck(turkey_adapter)

        print('\nThe drone adaper says...')
        drone_adapter.quack()
        drone_adapter.fly()

    @staticmethod
    def test_duck(duck: Duck) -> None:
        duck.quack()
        duck.fly()

if __name__ == '__main__':
    DuckTestDrive.main()
