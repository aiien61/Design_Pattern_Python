from icecream import ic

# Receiver
class GarageDoor:
    location: str

    def __init__(self):
        pass

    def up(self) -> None:
        ic('Garage Door is Open')

    def down(self) -> None:
        ic('Garage Door is Closed')

    def stop(self) -> None:
        ic('Garage Door is Stopped')

    def lightOn(self) -> None:
        ic('Garage Light is On')

    def lightOff(self) -> None:
        ic('Garage Light is Off')
