from HomeTheater.Subcomponents.Device import VisualDevice, PlayerDevice

class Screen:
    def __init__(self, description: str):
        self.description = description

    def up(self) -> None:
        print(f"{self.description} going up")

    def down(self) -> None:
        print(f"{self.description} going down")

    def __repr__(self):
        return self.description
    
class Projector(VisualDevice):
    def __init__(self, description: str, player: PlayerDevice):
        self.player = player
        self.description = description

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def __repr__(self):
        return self.description
    
    def wide_screen_mode(self) -> None:
        print(f"{self.description} in widescreen mode (16x9 aspect ratio)")

    def tv_mode(self) -> None:
        print(f"{self.description} in tv mode (4x3 aspect ratio)")
