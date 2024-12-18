from abc import ABC
from enum import Enum, auto
from icecream import ic


class LightLevel(Enum):
    OFF = auto()
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

class Light:
    def __init__(self, location: str):
        self.location = location
        self.level = LightLevel.OFF

    def on(self):
        self.level = LightLevel.HIGH
        ic('Light is on')
    
    def off(self):
        self.level = LightLevel.OFF
        ic('Light is off')

    def dim(self, level: LightLevel):
        self.level = level
        if self.level == LightLevel.OFF:
            self.off()
        else:
            print(f'Light is dimmed to {self.level.name}')
    
    def get_level(self):
        return self.level

class Command(ABC):
    def execute(self): raise NotImplementedError
    def undo(self): raise NotImplementedError
    

class NoCommand(Command):
    def execute(self): pass
    def undo(self): pass


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.level = self.light.get_level()
        self.light.on()

    def undo(self) -> None:
        self.light.dim(self.level)

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.level = self.light.get_level()
        self.light.off()

    def undo(self) -> None:
        self.light.dim(self.level)


class RemoteControlWithUndo:
    """Invoker"""
    slots: int = 7

    def __init__(self) -> None:
        self.on_commands = [NoCommand() for _ in range(self.slots)]
        self.off_commands = [NoCommand() for _ in range(self.slots)]
        self.undo_command = NoCommand()

    def set_command(self, slot_i: int, on_command: Command, off_command: Command) -> None:
        self.on_commands[slot_i] = on_command
        self.off_commands[slot_i] = off_command

    def on_button_pushed(self, slot_i: int):
        self.on_commands[slot_i].execute()
        self.undo_command = self.on_commands[slot_i]

    def off_button_pushed(self, slot_i: int):
        self.off_commands[slot_i].execute()
        self.undo_command = self.off_commands[slot_i]

    def undo_button_pushed(self):
        self.undo_command.undo()

    def __repr__(self) -> str:
        buffer = []
        buffer.append('\n----- Remote Control -----\n')
        for i, (on_command, off_command) in enumerate(zip(self.on_commands, self.off_commands)):
            buffer.append(f'[slot {i}] {on_command.__class__.__name__}   {off_command.__class__.__name__}\n')
        
        buffer.append(f'[undo] {self.undo_command.__class__.__name__}\n')
        return ''.join(buffer)
    
def remote_loader():
    # Initiate receivers, invoker, command instances
    remote_control = RemoteControlWithUndo()
    living_room_light = Light('Living Room')
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    # set command to connect receivers to the invoker
    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    ic(remote_control)

    remote_control.on_button_pushed(0)
    remote_control.off_button_pushed(0)
    
    ic(remote_control)
    remote_control.undo_button_pushed()

    remote_control.off_button_pushed(0)
    remote_control.on_button_pushed(0)
    ic(remote_control)

    remote_control.undo_button_pushed()

if __name__ == '__main__':
    remote_loader()
