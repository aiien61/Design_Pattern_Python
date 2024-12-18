from CeilingFan import CeilingFan
from CeilingFanOnCommand import CeilingFanOnCommand
from CeilingFanOffCommand import CeilingFanOffCommand
from RemoteControl import RemoteControl
from GarageDoor import GarageDoor
from GarageDoorUpCommand import GarageDoorUpCommand
from GarageDoorDownCommand import GarageDoorDownCommand
from Light import Light
from LightOnCommand import LightOnCommand
from LightOffCommand import LightOffCommand
from Stereo import Stereo
from StereoOnCommand import StereoOnCommand
from StereoOffCommand import StereoOffCommand
from StereoOnWithCDCommand import StereoOnWithCDCommand
from LivingroomLightOnCommand import LivingroomLightOnCommand
from LivingroomLightOffCommand import LivingroomLightOffCommand
from icecream import ic

class RemoteLoader:
    @staticmethod
    def main(*args) -> None:
        remote_control: RemoteControl = RemoteControl()

        livingroom_light: Light = Light('Living Room')
        kitchen_light: Light = Light('Kitchen')
        ceiling_fan: CeilingFan = CeilingFan('Living Room')
        garage_door: GarageDoor = GarageDoor('Garage')
        stereo: Stereo = Stereo('Living Room')

        livingroom_light_on: LightOnCommand = LightOnCommand(livingroom_light)
        livingroom_light_off: LightOffCommand = LightOffCommand(livingroom_light)
        kitchen_light_on: LightOnCommand = LightOnCommand(kitchen_light)
        kitchen_light_off: LightOffCommand = LightOffCommand(kitchen_light)

        ceiling_fan_on: CeilingFanOnCommand = CeilingFanOnCommand(ceiling_fan)
        ceiling_fan_off: CeilingFanOffCommand = CeilingFanOffCommand(ceiling_fan)

        garage_door_up: GarageDoorUpCommand = GarageDoorUpCommand(garage_door)
        garage_door_down: GarageDoorDownCommand = GarageDoorDownCommand(garage_door)

        stereo_on_with_CD: StereoOnWithCDCommand = StereoOnWithCDCommand(stereo)
        stereo_off: StereoOffCommand = StereoOffCommand(stereo)

        remote_control.set_command(0, livingroom_light_on, livingroom_light_off)
        remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
        remote_control.set_command(2, ceiling_fan_on, ceiling_fan_off)
        remote_control.set_command(3, stereo_on_with_CD, stereo_off)

        ic(remote_control.to_string())

        remote_control.on_button_pushed(0)
        remote_control.off_button_pushed(0)
        remote_control.on_button_pushed(1)
        remote_control.off_button_pushed(1)
        remote_control.on_button_pushed(2)
        remote_control.off_button_pushed(2)
        remote_control.on_button_pushed(3)
        remote_control.off_button_pushed(3)

if __name__ == '__main__':
    RemoteLoader.main()
