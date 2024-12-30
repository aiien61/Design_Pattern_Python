from HomeTheater.Subcomponents.Device import RadioDevice, AudioDevice

class Tuner(RadioDevice):
    def __init__(self, description: str, amplifier: AudioDevice):
        self.description = description
        self.frequency: float = None
        self.amp = amplifier

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def __repr__(self):
        return self.description
    
    def set_frequency(self, frequency: float) -> None:
        print(f"{self.description} setting frequency to {frequency}")
        self.frequency = frequency

    def set_am(self) -> None:
        print(f"{self.description} setting AM mode")

    def set_fm(self) -> None:
        print(f"{self.description} setting FM mode")
