from abc import ABC, abstractmethod

class Drone(ABC):
    @abstractmethod
    def beep(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def spin_rotors(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def take_off(self) -> None:
        raise NotImplementedError\


class SuperDrone(Drone):
    def beep(self) -> None:
        print("Beep beep beep")

    def spin_rotors(self) -> None:
        print("Rotors are spinning")

    def take_off(self) -> None:
        print("Taking off")
