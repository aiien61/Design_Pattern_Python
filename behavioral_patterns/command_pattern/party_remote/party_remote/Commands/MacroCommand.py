from typing import List
from party_remote.Commands.Command import Command

class MacroCommand(Command):
    commands: List[Command]

    def __init__(self, commands: List[Command]):
        self.commands = commands

    def execute(self) -> None:
        for i in range(len(self.commands)):
            self.commands[i].execute()

    def undo(self) -> None:
        for i in range(len(self.commands)):
            self.commands[i].undo()