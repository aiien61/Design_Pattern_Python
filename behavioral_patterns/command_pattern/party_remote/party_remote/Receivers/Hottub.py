class Hottub:
    on_: bool
    temperature: int = 0

    def __init__(self):
        pass

    def on(self) -> None:
        self.on_ = True

    def off(self) -> None:
        self.on_ = False

    def circulate(self) -> None:
        if self.on_:
            print('Hottub is bubbling')

    def jets_on(self) -> None:
        if self.on_:
            print('Hottub jets are on')

    def jets_off(self) -> None:
        if not self.on_:
            print('Hottub jets are off')

    def set_temperature(self, temperature: int) -> None:
        if temperature > self.temperature:
            print(f'Hottub is heating to steaming {self.temperature} degrees.')
        elif temperature < self.temperature:
            print(f'Hottub is cooling to {self.temperature} degrees.')
        self.temperature = temperature

