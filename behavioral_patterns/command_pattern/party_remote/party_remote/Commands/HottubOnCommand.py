from party_remote.Commands.Command import Command
from party_remote.Receivers.Hottub import Hottub

class HottubOnCommand(Command):
    hottub: Hottub

    def __init__(self, hottub: Hottub):
        self.hottub = hottub

    def execute(self) -> None:
        self.hottub.on()
        self.hottub.set_temperature(100)
        self.hottub.circulate()

    def undo(self) -> None:
        self.hottub.off()
