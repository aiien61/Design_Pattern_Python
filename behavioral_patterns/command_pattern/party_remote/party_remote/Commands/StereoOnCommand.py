from party_remote.Commands.Command import Command
from party_remote.Receivers.Stereo import Stereo


class StereoOnCommand(Command):
    stereo: Stereo

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.on()

    def undo(self) -> None:
        self.stereo.off()
