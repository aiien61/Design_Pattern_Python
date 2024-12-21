from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List
from icecream import ic


class LightLevel(Enum):
    OFF = 0
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class Light:
    """Receiver"""
    def __init__(self, location: str):
        self.location = location
        self.level = LightLevel.OFF

    def on(self) -> None:
        self.level = LightLevel.HIGH
        print(f"{self.location} light is on")
    
    def off(self) -> None:
        self.level = LightLevel.OFF
        print(f"{self.location} light is off")

    def dim(self, level: LightLevel) -> None:
        self.level = level
        if self.level == LightLevel.OFF:
            self.off()
        else:
            print(f"{self.location} light is dimmed to {self.level}")
    
    def get_level(self) -> LightLevel:
        return self.level


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError
    
    @abstractmethod
    def undo(self):
        raise NotImplementedError


class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.level = self.light.get_level()
        self.light.on()

    def undo(self):
        self.light.dim(self.level)


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.level = self.light.get_level()
        self.light.off()

    def undo(self):
        self.light.dim(self.level)


class RemoteControlWithUndo:
    """Invoker"""

    def __init__(self):
        self.on_commands: List[Command] = [NoCommand() for _ in range(7)]
        self.off_commands: List[Command] = [NoCommand() for _ in range(7)]
        self.undo_command = NoCommand()

    def set_command(self, i: int, on_command: Command, off_command: Command):
        self.on_commands[i] = on_command
        self.off_commands[i] = off_command

    def on_button_being_pushed(self, i: int):
        self.on_commands[i].execute()
        self.undo_command = self.on_commands[i]

    def off_button_being_pushed(self, i: int):
        self.off_commands[i].execute()
        self.undo_command = self.off_commands[i]

    def undo_button_being_pushed(self):
        self.undo_command.undo()

    def __repr__(self) -> str:
        buffer: List[str] = []
        buffer.append("\n----- Remote Control -----\n")
        for i, (on_command, off_command) in enumerate(zip(self.on_commands, self.off_commands)):
            buffer.append(f"[slot {i}] {on_command.__class__.__name__}\t{off_command.__class__.__name__}\n")
        buffer.append(f"[undo] {self.undo_command.__class__.__name__}\n")
        return "".join(buffer)


def remote_loader():
    remote_control = RemoteControlWithUndo()
    living_room_light = Light("Living Room")
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)

    ic(remote_control)
    
    remote_control.on_button_being_pushed(0)
    remote_control.off_button_being_pushed(0)
    ic(remote_control)

    remote_control.undo_button_being_pushed()
    remote_control.off_button_being_pushed(0)
    remote_control.on_button_being_pushed(0)
    ic(remote_control)

    remote_control.undo_button_being_pushed()

if __name__ == '__main__':
    remote_loader()
