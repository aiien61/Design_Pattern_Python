from HomeTheater.Subcomponents.Device import PlayerDevice, AudioDevice

class CDPlayer(PlayerDevice):
    def __init__(self, description: str, amplifier: AudioDevice):
        self.description = description
        self.amplifier = amplifier
        self.title: str = None
        self.current_track: int = 0

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def __repr__(self):
        return self.description
    
    def play(self, title: str) -> None:
        self.title = title
        self.current_track = 0
        print(f'{self.description} playing "{title}"')

    def play_track(self, track: int) -> None:
        if self.title is None:
            print(f"{self.description} can't play track {self.current_track}, no cd inserted")
        else:
            self.current_track = track
            print(f"{self.description} playing track {self.current_track}")
    
    def stop(self) -> None:
        self.current_track = 0
        print(f"{self.description} stopped")
    
    def pause(self) -> None:
        self.current_track = 0
        print(f'{self.description} paused "{self.title}"')


class StreamingPlayer(PlayerDevice):
    def __init__(self, description: str, amplifier: AudioDevice):
        self.description = description
        self.amplifier = amplifier
        self.current_chapter: int = 0
        self.movie: str = None

    def on(self) -> None:
        print(f"{self.description} on")

    def off(self) -> None:
        print(f"{self.description} off")

    def __repr__(self):
        return self.description

    def play(self, movie: str) -> None:
        self.movie = movie
        self.current_chapter = 0
        print(f'{self.description} playing "{movie}"')

    def play_chapter(self, chapter: int) -> None:
        if self.movie is None:
            print(f"{self.description} can't play chapter {chapter} no movie selected")
        else:
            self.current_chapter = chapter
            print(f'{self.description} playing chapter {self.current_chapter} of "{self.movie}"')

    def stop(self) -> None:
        self.current_chapter = 0
        print(f'{self.description} stopped "{self.movie}"')
    
    def pause(self) -> None:
        self.current_chapter = 0
        print(f'{self.description} paused "{self.movie}"')

    def set_two_channel_audtio(self) -> None:
        print(f"{self.description} set two channel audio")

    def set_surround_audio(self) -> None:
        print(f"{self.description} set surround audio")
