from Command import Command
from Stereo import Stereo

class StereoOnWithCDCommand(Command):
    stereo: Stereo

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.on()
        self.stereo.set_CD()
        self.stereo.set_volume(11)