# If there are more actions in Light class, what we need to change or adjust is 
# create more concrete command classes, and don't need to do anything on the invoker class

# Receiver defines the logic after the execution
# The object being manipulated under the execution
class Light:
    def turn_on(self):
        print('The light is ON')

    def turn_off(self):
        print('The light is OFF')

# Command Interface
# In order to make sure that all actions from the receiver can be encapsulated 
# into identical interfaces for any command senders
class Command:
    def execute(self):
        raise NotImplementedError('Subclasses must implement "execute" method')
    
    def undo(self):
        raise NotImplementedError('Subclasses must implement "undo" method')

# Concrete TurnOn Command Class
# Concrete Command Class can seen as a bridge that is used to decouple between commands and executions, 
# and can be reset if needed
class TurnOnLightCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

# Concrete TurnOff Command Class
# Concrete Command Class can seen as a bridge that is used to decouple between commands and executions,
# and can be reset if needed
class TurnOffLightCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Invoker Instance will be responsible for executing the command
# Responsible for passing commands from users to receivers, e.g. a remote between humans viewers and a telly
class RemoteControl:
    def __init__(self):
        self.command = None
    
    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

    def press_undo(self):
        if self.command:
            self.command.undo()

if __name__ == '__main__':
    # Create a receiver instance
    light = Light()

    # Create commands
    turn_on_command = TurnOnLightCommand(light)
    turn_off_command = TurnOffLightCommand(light)

    # Create an invoker instance
    remote = RemoteControl()

    # Execute turn-on command
    remote.set_command(turn_on_command)
    remote.press_button()
    remote.press_undo()

    # Execute turn-off command
    remote.set_command(turn_off_command)
    remote.press_button()
    remote.press_undo()
