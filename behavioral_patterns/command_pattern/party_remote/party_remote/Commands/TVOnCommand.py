from party_remote.Commands.Command import Command
from party_remote.Receivers.TV import TV


class TVOnCommand(Command):
    tv: TV

    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self) -> None:
        self.tv.on()
        self.tv.set_input_channel()

    def undo(self) -> None:
        self.tv.off()
