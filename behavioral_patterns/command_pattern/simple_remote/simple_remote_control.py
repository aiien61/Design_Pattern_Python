from command import Command

# Invoker
class SimpleRemoteCommand:
    slot: Command

    def __init__(self):
        pass

    def set_command(self, command: Command) -> None:
        self.slot = command

    def press_button(self) -> None:
        self.slot.execute()
