from HomeTheater.Subcomponents.Device import AudioDevice, RadioDevice, PlayerDevice

class Amplifier(AudioDevice):
    description: str
    tuner: RadioDevice
    player: PlayerDevice

    def __init__(self, description: str):
        self.description = description

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def __repr__(self):
        return self.description

    def set_stereo_sound(self) -> None:
        print(f"{self.description} stereo mode on")
    
    def set_surround_sound(self) -> None:
        print(f"{self.description} surround mode on (5 speakers, 1 subwoofer)")

    def set_volume(self, level: int) -> None:
        print(f"{self.description} setting volume to {level}")

    def set_tuner(self, tuner: RadioDevice) -> None:
        print(f"{self.description} setting tuner to {tuner}")
        self.tuner = tuner

    def set_streaming_player(self, player: PlayerDevice) -> None:
        print(f"{self.description} setting streaming player to {player}")
        self.player = player
