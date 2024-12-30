class PopcornPopper:
    def __init__(self, description: str):
        self.description = description

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def pop(self) -> None:
        print(f"{self.description} popping popcorn")

    def __repr__(self):
        return self.description
