import sys
from party_remote.Commands.Command import Command
from party_remote.Receivers.CeilingFan import CeilingFan


class CeilingFanOffCommand(Command):
    ceiling_fan: CeilingFan
    prev_speed: CeilingFan.Speed = CeilingFan.Speed.OFF

    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.off()

    def undo(self) -> None:
        version = sys.version_info
        if version.major == 3 and version.minor >= 10:
            match self.prev_speed:
                case CeilingFan.Speed.HIGH.name: self.ceiling_fan.high()
                case CeilingFan.Speed.MEDIUM.name: self.ceiling_fan.medium()
                case CeilingFan.Speed.LOW.name: self.ceiling_fan.low()
                case _: self.ceiling_fan.off()
        else:
            if self.prev_speed == CeilingFan.Speed.HIGH.name:
                self.ceiling_fan.high()
            elif self.prev_speed == CeilingFan.Speed.MEDIUM.name:
                self.ceiling_fan.medium()
            elif self.prev_speed == CeilingFan.Speed.LOW.name:
                self.ceiling_fan.low()
            else:
                self.ceiling_fan.off()
