from HomeTheater.Subcomponents.Device import LightingDevice

class TheaterLights(LightingDevice):
    def __init__(self, description: str):
        self.description = description

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def __repr__(self):
        return self.description
    
    def dim(self, level: int) -> None:
        print(f"{self.description} dimming to {level}%")
