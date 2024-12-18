from icecream import ic

class TV:
    location: str
    channel: int

    def __init__(self, location: str):
        self.location = location
    
    def on(self) -> None:
        ic('TV is on')

    def off(self) -> None:
        ic('TV is off')

    def set_input_channel(self) -> None:
        self.channel = 3
        ic('Channel is set for VCR')