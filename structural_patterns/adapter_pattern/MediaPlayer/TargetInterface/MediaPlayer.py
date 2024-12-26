from abc import ABC, abstractmethod

# The client's expected interface
# can't be directly used
class MediaPlayer(ABC):
    """Target Interface"""
    @abstractmethod
    def play(self, audio_type: str, file_name: str):
        raise NotImplementedError