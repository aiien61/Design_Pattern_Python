from typing import List

from party_remote.Commands.Command import Command
from party_remote.Commands.NoCommand import NoCommand

class RemoteControl:
    on_commands: List[Command]
    off_commands: List[Command]
    undo_command: Command

    def __init__(self):
        self.on_commands = [None] * 7
        self.off_commands = [None] * 7
        no_command: Command = NoCommand()

        for i in range(7):
            self.on_commands[i] = no_command
            self.off_commands[i] = no_command
        self.undo_command = no_command

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pushed(self, slot: int) -> None:
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_pushed(self, slot: int) -> None:
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def to_string(self) -> str:
        string_buffer: StringBuffer = StringBuffer()
        string_buffer.append("\n----- Remote Control -----\n")
        for i in range(len(self.on_commands)):
            string_buffer.append(f"[slot {i}] {self.on_commands[i].__class__.__name__:25s}{self.off_commands[i].__class__.__name__}\n")
        string_buffer.append(f"[undo] {self.undo_command.__class__.__name__}\n")
        return string_buffer.to_string()


class StringBuffer:
    def __init__(self):
        self.ls: List[str] = []

    def append(self, string: str) -> None:
        self.ls.append(string)

    def to_string(self) -> str:
        return ''.join(self.ls)
