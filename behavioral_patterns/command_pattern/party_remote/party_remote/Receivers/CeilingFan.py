from typing import Final
from enum import Enum, auto

class CeilingFan:
    class Speed(Enum):
        OFF: Final[int] = 0
        LOW: Final[int] = auto()
        MEDIUM: Final[int] = auto()
        HIGH: Final[int] = auto()

    location: str = ""
    speed: Speed = Speed.OFF

    def __init__(self, location: str):
        self.location = location

    def high(self) -> None:
        """Turn the ceiling fan to speed HIGH"""
        self.speed = CeilingFan.Speed.HIGH
        print(f'{self.location} ceiling fan is on {self.speed.name}')

    def medium(self) -> None:
        """Turn the ceiling fan to speed MEDIUM"""
        self.speed = CeilingFan.Speed.MEDIUM
        print(f'{self.location} ceiling fan is on {self.speed.name}')

    def low(self) -> None:
        """Turn the ceiling fan to speed LOW"""
        self.speed = CeilingFan.Speed.LOW
        print(f'{self.location} ceiling fan is on {self.speed.name}')

    def off(self) -> None:
        """Turn off the ceiling fan"""
        self.speed = CeilingFan.Speed.OFF
        print(f'{self.location} ceiling fan is on {self.speed.name}')

    def get_speed(self) -> int:
        return self.speed.name

