from typing import List

from party_remote.Commands.Command import Command
from RemoteControl import RemoteControl
from party_remote.Commands.MacroCommand import MacroCommand

from party_remote.Receivers.Light import Light
from party_remote.Commands.LightOnCommand import LightOnCommand
from party_remote.Commands.LightOffCommand import LightOffCommand

from party_remote.Receivers.Stereo import Stereo
from party_remote.Commands.StereoOnCommand import StereoOnCommand
from party_remote.Commands.StereoOffCommand import StereoOffCommand

from party_remote.Receivers.TV import TV
from party_remote.Commands.TVOnCommand import TVOnCommand
from party_remote.Commands.TVOffCommand import TVOffCommand

from party_remote.Receivers.Hottub import Hottub
from party_remote.Commands.HottubOnCommand import HottubOnCommand
from party_remote.Commands.HottubOffCommand import HottubOffCommand


class RemoteLoader:
    @staticmethod
    def main(*args) -> None:
        remote_control: RemoteControl = RemoteControl()

        light: Light = Light('Living Room')
        tv: TV = TV('Living Room')
        stereo: Stereo = Stereo('Living Room')
        hottub: Hottub = Hottub()

        light_on: LightOnCommand = LightOnCommand(light)
        light_off: LightOffCommand = LightOffCommand(light)

        stereo_on: StereoOnCommand = StereoOnCommand(stereo)
        stereo_off: StereoOffCommand = StereoOffCommand(stereo)

        tv_on: TVOnCommand = TVOnCommand(tv)
        tv_off: TVOffCommand = TVOffCommand(tv)

        hottub_on: HottubOnCommand = HottubOnCommand(hottub)
        hottub_off: HottubOffCommand = HottubOffCommand(hottub)

        party_on: List[Command] = [light_on, stereo_on, tv_on, hottub_on]
        party_off: List[Command] = [light_off, stereo_off, tv_off, hottub_off]

        party_on_macro: MacroCommand = MacroCommand(party_on)
        party_off_macro: MacroCommand = MacroCommand(party_off)

        remote_control.set_command(0, party_on_macro, party_off_macro)

        print(remote_control.to_string())
        print('Pushing Macro On'.center(30, '-'))
        remote_control.on_button_pushed(0)
        print('Pushing Macro Off'.center(30, '-'))
        remote_control.off_button_pushed(0)

if __name__ == '__main__':
    RemoteLoader.main()
