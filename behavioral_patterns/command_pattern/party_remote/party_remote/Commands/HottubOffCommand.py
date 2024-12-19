from party_remote.Commands.Command import Command
from party_remote.Receivers.Hottub import Hottub

class HottubOffCommand(Command):
    hottub: Hottub

    def __init__(self, hottub: Hottub):
        self.hottub = hottub
    
    def execute(self) -> None:
        self.hottub.set_temperature(98)
        self.hottub.off()

    def undo(self) -> None:
        self.hottub.on()
