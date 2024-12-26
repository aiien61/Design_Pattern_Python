from MediaPlayer.Adaptee.ThirdPartyPlayer import ThirdPartyPlayer
from MediaPlayer.TargetInterface.MediaPlayer import MediaPlayer

# Adapter class: 
# actual interface for clients to convert third party player into media player
class MediaPlayerAdapter(MediaPlayer):
    """Adapter"""
    def __init__(self, third_party_player: ThirdPartyPlayer):
        self.third_party_player = third_party_player
    
    def play(self, audio_type: str, file_name: str):
        match audio_type:
            case 'mp3': self.third_party_player.play_mp3(file_name)
            case 'flac': self.third_party_player.play_flac(file_name)
            case _: print(f'Audio type {audio_type} not supported.')
