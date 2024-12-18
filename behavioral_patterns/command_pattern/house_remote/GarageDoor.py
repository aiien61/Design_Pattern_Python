
# Receiver
class GarageDoor:
    location: str

    def __init__(self, location: str):
        self.location = location

    def up(self) -> None:
        print(f'{self.location} garage door is up')

    def down(self) -> None:
        print(f'{self.location} garage door is down')

    def stop(self) -> None:
        print(f'{self.location} garage door is stopped')

    def light_on(self) -> None:
        print(f'{self.location} garage light is on')

    def light_off(self) -> None:
        print(f'{self.location} garage light is off')
