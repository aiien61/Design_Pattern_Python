from Command import Command
from GarageDoor import GarageDoor

class GarageDoorUpCommand(Command):
    garage_door: GarageDoor

    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.up()