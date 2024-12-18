class Stereo:
    location: str

    def __init__(self, location: str):
        self.location = location

    def on(self) -> None:
        print(f'{self.location} stereo is on')

    def off(self) -> None:
        print(f'{self.location} stereo is off')
    
    def set_CD(self) -> None:
        print(f'{self.location} stereo is set for CD input')

    def set_DVD(self) -> None:
        print(f'{self.location} stereo is set for DVD input')
    
    def set_radio(self) -> None:
        print(f'{self.location} stereo is set for radio')
    
    def set_volume(self, volume: int) -> None:
        print(f'{self.location} stereo volume set to {volume}')
