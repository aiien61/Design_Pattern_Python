from MediaPlayer.Adaptee.ThirdPartyPlayer import ThirdPartyPlayer
from MediaPlayer.Adapter.MediaPlayerAdapter import MediaPlayerAdapter
from MediaPlayer.TargetInterface.MediaPlayer import MediaPlayer

if __name__ == '__main__':
    # the third party player
    third_party_player: ThirdPartyPlayer = ThirdPartyPlayer()

    # adapter
    player_adapter: MediaPlayer = MediaPlayerAdapter(third_party_player)

    # use adapter to play music
    player_adapter.play("mp3", "milet_songs.mp3")
    player_adapter.play("flac", "milet_songs.flac")
    player_adapter.play("wav", "milet.wav")
