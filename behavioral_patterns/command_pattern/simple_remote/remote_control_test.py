from garage_door import GarageDoor
from garage_door_command import GarageDoorCommand
from light import Light
from light_on_command import LightOnCommand
from light_off_command import LightOffCommand
from simple_remote_control import SimpleRemoteCommand

class RemoteControlTest:
    @staticmethod
    def main(*argw) -> None:
        remote: SimpleRemoteCommand = SimpleRemoteCommand()

        light: Light = Light()
        garagedoor: GarageDoor = GarageDoor()

        lightOn: LightOnCommand = LightOnCommand(light)
        lightOff: LightOffCommand = LightOffCommand(light)
        garageOpen: GarageDoorCommand = GarageDoorCommand(garagedoor)

        remote.set_command(lightOn)
        remote.press_button()

        remote.set_command(lightOff)
        remote.press_button()

        remote.set_command(garageOpen)
        remote.press_button()

if __name__ == '__main__':
    RemoteControlTest.main()
