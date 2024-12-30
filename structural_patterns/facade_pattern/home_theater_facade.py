from abc import ABC, abstractmethod
from typing import Dict
from icecream import ic

class SoundDevice(ABC):
    @abstractmethod
    def on(self): raise NotImplementedError

    @abstractmethod
    def off(sefl): raise NotImplementedError

    @abstractmethod
    def set_volume(self): raise NotImplementedError

class PlayerDevice(ABC):
    @abstractmethod
    def on(self): raise NotImplementedError

    @abstractmethod
    def off(sefl): raise NotImplementedError

    @abstractmethod
    def play(self): raise NotImplementedError

    @abstractmethod
    def stop(self): raise NotImplementedError

    @abstractmethod
    def pause(self): raise NotImplementedError

class TunerDevice(ABC):
    @abstractmethod
    def on(self): raise NotImplementedError

    @abstractmethod
    def off(sefl): raise NotImplementedError

# subcomponents
class Amplifier(SoundDevice):
    def __init__(self, description: str):
        self.description = description
        self.tuner = None
        self.player = None

    def __repr__(self):
        return self.description
    
    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def set_stereo_sound(self):
        print(f"{self.description} stereo mode on")

    def set_surround_sound(self):
        print(f"{self.description} surround sound on (5 speakers, 1 subwoofer)")

    def set_volume(self, level: int):
        print(f"{self.description} setting volume to {level}")

    def set_tuner(self, tuner: TunerDevice):
        print(f"{self.description} setting tuner to {tuner}")
        self.tuner = tuner

    def set_streaming_player(self, player: PlayerDevice):
        print(f"{self.description} setting streaming player to {player}")
        self.player = player

class Tuner(TunerDevice):
    def __init__(self, description: str, amplifier: SoundDevice):
        self.description = description
        self.amplifier = amplifier
        self.frequency = None

    def __repr__(self):
        return self.description
    
    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def set_frequency(self, frequency: str):
        print(f"{self.description} setting frequency to {frequency}")
        self.frequency = frequency

    def set_am(self):
        print(f"{self.description} setting AM mode")

    def set_fm(self):
        print(f"{self.description} setting FM mode")

class StreamingPlayer:
    def __init__(self, description: str, amplifier: Amplifier):
        self.description = description
        self.amplifier = amplifier
        self.current_chapter = 0
        self.movie = None

    def __repr__(self):
        return self.description
    
    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def play(self, arg):
        if isinstance(arg, str):
            self.movie = arg
            self.current_chapter = 0
            print(f'{self.description} playing "{self.movie}"')
        elif isinstance(arg, int):
            if self.movie is None:
                print(f"{self.description} can't play chapter {arg} no movie selected")
            else:
                self.current_chapter = arg
                print(f'{self.description} playing chapter {self.current_chapter} of "{self.movie}"')
    
    def stop(self):
        self.current_chapter = 0
        print(f'{self.description} stopped "{self.movie}"')
    
    def pause(self):
        print(f'{self.description} paused "{self.movie}"')

    def set_two_channel_audio(self):
        print(f"{self.description} set two channel audio")

    def set_surround_audio(self):
        print(f"{self.description} set surround audio")

class CDPlayer:
    def __init__(self, description: str, amplifier: Amplifier):
        self.description = description
        self.current_track = 0
        self.amplifier = amplifier
        self.title = None

    def __repr__(self):
        return self.description
    
    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def play(self, arg):
        if isinstance(arg, str):
            self.title = arg
            self.current_track = 0
            print(f'{self.description} playing "{self.title}"')
        elif isinstance(arg, int):
            if self.title is None:
                print(f"{self.description} can't play track {self.current_track}, no cd inserted")
            else:
                self.current_track = arg
                print(f'{self.description} playing track {self.current_track}')

    def eject(self):
        print(f"{self.description} eject")
    
    def stop(self):
        print(f'{self.description} stopped')

    def pause(self):
        print(f'{self.description} paused')

class Projector:
    def __init__(self, description: str, player: PlayerDevice):
        self.description = description
        self.player = player

    def __repr__(self):
        return self.description
    
    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def wide_screen_mode(self):
        print(f"{self.description} in widescreen mode (16x9 aspect ratio)")

    def tv_mode(self):
        print(f"{self.description} in tv mode (4x3 aspect ratio)")

class Screen:
    def __init__(self, description: str):
        self.description = description

    def __repr__(self):
        return self.description
    
    def up(self):
        print(f"{self.description} going up")

    def down(self):
        print(f"{self.description} going down")

class TheaterLights:
    def __init__(self, description: str):
        self.description = description

    def __repr__(self):
        return self.description
    
    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def dim(self, level: int):
        print(f"{self.description} dimming to {level}%")

class PopcornPopper:
    def __init__(self, description: str):
        self.description = description

    def __repr__(self):
        return self.description

    def on(self):
        print(f"{self.description} on")

    def off(self):
        print(f"{self.description} off")

    def pop(self):
        print(f"{self.description} popping popcorn")

# Facade pattern
class HomeTheaterFacade:
    """Connect all the subcomponents to make theatre system easier to use."""

    def __init__(self, **subcomponents):
        self.amp = subcomponents.get('amplifier')
        self.tuner = subcomponents.get('tuner')
        self.player = subcomponents.get('player')
        self.projector = subcomponents.get('projector')
        self.screen = subcomponents.get('screen')
        self.lights = subcomponents.get('lights')
        self.popper = subcomponents.get('popper')

    def watch_movie(self, movie: str):
        print('Get ready to watch a movie...')
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_streaming_player(self.player)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.player.on()
        self.player.play(movie)
    
    def end_movie(self):
        print("Shutting movie theatre down...")
        self.popper.off()
        self.lights.off()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()

    def listen_to_radio(self, frequency: str):
        print("Tuning in the airwaves...")
        self.tuner.on()
        self.tuner.set_frequency(frequency)
        self.amp.on()
        self.amp.set_volume(5)
        self.amp.set_tuner(self.tuner)

    def end_radio(self):
        print('Shutting down the tuner...')
        self.tuner.off()
        self.amp.off()

# Test 
def theater_test_drive():
    amp: SoundDevice = Amplifier("Amplifier")
    tuner: TunerDevice = Tuner("AM/FM Tuner", amp)
    player: PlayerDevice = StreamingPlayer("Streaming Player", amp)
    projector: Projector = Projector("Projector", player)
    lights: TheaterLights = TheaterLights("Theatre Ceiling Lights")
    screen: Screen = Screen("Theatre Screen")
    popper: PopcornPopper = PopcornPopper("Popcorn Popper")

    subcomponents: Dict[str, object] = {
        'amplifier': amp,
        'tuner': tuner,
        'player': player,
        'projector': projector,
        'lights': lights,
        'screen': screen,
        'popper': popper
    }

    home_theatre = HomeTheaterFacade(**subcomponents)
    ic('Start watching movie...')
    home_theatre.watch_movie("The Internship")
    ic('Stop wathcing movie...')
    home_theatre.end_movie()

if __name__ == '__main__':
    theater_test_drive()
