# Third party class that can't support client's features
class ThirdPartyPlayer:
    """Adaptee"""
    def play_mp3(self, file_name: str) -> None:
        print(f"Playing MP3 file: {file_name}")

    def play_flac(self, file_name: str) -> None:
        print(f"Playing FLAC file: {file_name}")