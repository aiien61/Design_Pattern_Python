from CeilingFan import CeilingFan
from Command import Command


class CeilingFanOffCommand(Command):
    ceiling_fan: CeilingFan

    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan
    
    def execute(self) -> None:
        self.ceiling_fan.off()
