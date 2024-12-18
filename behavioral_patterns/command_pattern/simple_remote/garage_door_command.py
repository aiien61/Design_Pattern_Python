from command import Command
from garage_door import GarageDoor

# Garage Door Command Class
class GarageDoorCommand(Command):
    def __init__(self, garagedoor: GarageDoor):
        self.garagedoor = garagedoor

    def execute(self) -> None:
        self.garagedoor.up()
