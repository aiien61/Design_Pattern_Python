from icecream import ic

# Receiver
class Hottub:
    on_: bool
    temperature: int

    def __init__(self):
        pass

    def on(self) -> None:
        self.on_ = True

    def off(self) -> None:
        self.on_ = False

    def bubbles_on(self) -> None:
        if self.on_:
            ic('Hottub is bubbling')

    def bubbles_off(self) -> None:
        if not self.on_:
            ic('Hottub is not bubbling')

    def jets_on(self) -> None:
        if self.on_:
            ic('Hottub jets are on')

    def jets_off(self) -> None:
        if not self.on_:
            ic('Hottub jets are off')

    def set_temperature(self, temperature: int) -> None:
        self.temperature = temperature

    def heat(self) -> None:
        self.temperature = 105
        ic('Hottub is heating to a steaming 105 degrees')

    def cool(self) -> None:
        self.temperature = 98
        ic('Hottub is cooling to 98 degrees')
