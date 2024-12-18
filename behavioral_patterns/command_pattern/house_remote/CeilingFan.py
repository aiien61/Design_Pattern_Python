from typing import Final
from icecream import ic

# Receiver
class CeilingFan:
    location: str = ""
    level: int
    HIGH: Final[int] = 2
    MEDIUM: Final[int] = 1
    LOW: Final[int] = 0

    def __init__(self, location: str):
        self.location = location

    def high(self) -> None:
        self.level = self.HIGH
        print(f'{self.location} ceiling fan is on high')

    def medium(self) -> None:
        self.level = self.MEDIUM
        print(f'{self.location} ceiling fan is on medium')

    def low(self) -> None:
        self.level = self.LOW
        print(f'{self.location} ceiling fan is low')

    def off(self) -> None:
        self.level = 0
        print(f'{self.location} ceiling fan is off')

    def get_speed(self) -> int:
        return self.level
