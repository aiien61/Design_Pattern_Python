from HomeTheater.Subcomponents.AudioDevice import Amplifier
from HomeTheater.Subcomponents.Popcorn import PopcornPopper
from HomeTheater.Subcomponents.Device import RadioDevice, PlayerDevice, VisualDevice, LightingDevice

class HomeTheaterFacade:
    def __init__(self, **components):
        self.amp: Amplifier = components.get('amplifier')
        self.tuner: RadioDevice = components.get('tuner')
        self.player: PlayerDevice = components.get('player')
        self.projector: VisualDevice = components.get('projector')
        self.screen: VisualDevice = components.get('screen')
        self.lights: LightingDevice = components.get('lights')
        self.popper: PopcornPopper = components.get('popper')

    def watch_movie(self, movie: str) -> None:
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(5)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_streaming_player(self.player)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.player.on()
        self.player.play(movie)

    def end_movie(self) -> None:
        print("Shutting movie theatre down...")
        self.popper.off()
        self.lights.off()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()

    def listen_to_radio(self, frequency: float) -> None:
        print("Tuning in the airwaves...")
        self.tuner.on()
        self.tuner.set_frequency(frequency)
        self.amp.on()
        self.amp.set_volume(5)
        self.amp.set_tuner(self.tuner)

    def end_radio(self) -> None:
        print("Shutting down the tuner...")
        self.tuner.off()
        self.amp.off()
