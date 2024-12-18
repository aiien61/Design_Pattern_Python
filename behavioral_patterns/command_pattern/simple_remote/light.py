from icecream import ic

# Receiver
class Light:
    location: str = ""

    def __init__(self):
        pass

    def on(self) -> None:
        ic('Light is On')

    def off(self) -> None:
        ic('Light is Off')
