from typing import List
from Command import Command
from NoCommand import NoCommand

class StringBuffer:
    def __init__(self):
        self.ls = []

    def append(self, string: str) -> None:
        self.ls.append(string)

    def to_string(self) -> str:
        return ''.join(self.ls)


class RemoteControl:
    on_commands: List[Command]
    off_commands: List[Command]

    def __init__(self):
        self.on_commands = [None] * 7
        self.off_commands = [None] * 7
        no_command: Command = NoCommand()
        for i in range(7):
            self.on_commands[i] = no_command
            self.off_commands[i] = no_command

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pushed(self, slot: int) -> None:
        self.on_commands[slot].execute()

    def off_button_pushed(self, slot: int) -> None:
        self.off_commands[slot].execute()

    def to_string(self) -> str:
        string_buff: StringBuffer = StringBuffer()
        string_buff.append("\n----- Remote Control -----\n")
        for i in range(len(self.on_commands)):
            string_buff.append(f'[slot {i}] {self.on_commands[i].__class__.__name__:25s}{self.off_commands[i].__class__.__name__}\n')
        return string_buff.to_string()

