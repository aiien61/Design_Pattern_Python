from DuckTurkeyAdapter.Adaptee.Drone import Drone
from DuckTurkeyAdapter.Adaptee.Duck import Duck

class DroneAdapter(Duck):
    """Drone to Duck"""
    def __init__(self, drone: Drone):
        self.drone = drone

    def quack(self) -> None:
        self.drone.beep()
        return None

    def fly(self) -> None:
        self.drone.spin_rotors()
        self.drone.take_off()
        return None
