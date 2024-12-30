from HomeTheater.Subcomponents.AudioDevice import Amplifier
from HomeTheater.Subcomponents.LightingDevice import TheaterLights
from HomeTheater.Subcomponents.PlayerDevice import StreamingPlayer, CDPlayer
from HomeTheater.Subcomponents.Popcorn import PopcornPopper
from HomeTheater.Subcomponents.RadioDevice import Tuner
from HomeTheater.Subcomponents.VisualDevice import Screen, Projector
from HomeTheater.Facade.HomeTheaterFacade import HomeTheaterFacade
from typing import Dict
from icecream import ic

class HomeTheaterTestDrive:
    @staticmethod
    def main(*args):
        amp: Amplifier = Amplifier("Amplifier")
        tuner: Tuner = Tuner("AM/FM Tuner", amp)
        player: StreamingPlayer = StreamingPlayer("Streaming Player", amp)
        cd: CDPlayer = CDPlayer("CD Player", amp)
        projector: Projector = Projector("Projector", player)
        lights: TheaterLights = TheaterLights("Theatre Ceiling Lights")
        screen: Screen = Screen("Theatre Screen")
        popper: PopcornPopper = PopcornPopper("Popcorn Popper")

        subcomponents: Dict[str, object] = {
            'amplifier': amp,
            'tuner': tuner,
            'player': player,
            'cd': cd,
            'projector': projector,
            'lights': lights,
            'screen': screen,
            'popper': popper
        }

        home_theater: HomeTheaterFacade = HomeTheaterFacade(**subcomponents)
        ic('Start to watch movie...')
        home_theater.watch_movie("The Internship")
        ic('Stop watching movie...')
        home_theater.end_movie()

if __name__ == '__main__':
    HomeTheaterTestDrive.main()
