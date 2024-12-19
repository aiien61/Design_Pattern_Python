from party_remote.Commands.Command import Command
from party_remote.Receivers.Stereo import Stereo


class StereoOffCommand(Command):
    stereo: Stereo

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.off()

    def undo(self) -> None:
        self.stereo.on()