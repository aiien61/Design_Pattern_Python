from abc import ABC, abstractmethod
from typing import Optional

class TV(ABC):
    @abstractmethod
    def on(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def off(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def tune_channel(self, channel: int) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def get_channel(self) -> int:
        raise NotImplementedError


class Sony(TV):
    station: int = 0

    def on(self) -> None:
        print("Turning on the Sony TV")

    def off(self) -> None:
        print("Turning off the Sony TV")

    def tune_channel(self, channel: int) -> None:
        self.station = channel
        print(f"Set the Sony TV station to {self.station}")

    def get_channel(self) -> int:
        return self.station
    
class LG(TV):
    channel: int = 1

    def on(self) -> None:
        print("Turning on the LG TV")

    def off(self) -> None:
        print("Turning off the LG TV")

    def tune_channel(self, channel: int) -> None:
        self.channel = channel
        print(f"Set the LG TV station to {self.channel}")

    def get_channel(self) -> int:
        return self.channel

class TVFactory:
    def get_TV(self, type_: str) -> TV:
        tv: TV = None

        match type_:
            case "LG": tv = LG()
            case "Sony": tv = Sony()
            case _: raise Exception("Invalid TV Type")
        return tv

class RemoteControl(ABC):
    tv: TV

    def __init__(self, tv_factory: TVFactory):
        self.tv_factory = tv_factory
        self.tv: Optional[TV] = None

    def on(self) -> None:
        self.tv.on()

    def off(self) -> None:
        self.tv.off()

    def set_channel(self, channel: int) -> None:
        self.tv.tune_channel(channel)

    def get_channel(self) -> int:
        return self.tv.get_channel()
    
    def set_TV(self, type_: str) -> None:
        try:
            self.tv = self.tv_factory.get_TV(type_)
        except Exception as e:
            print(e)

class GenericRemote(RemoteControl):
    def __init__(self, tv_factory: TVFactory):
        super().__init__(tv_factory)

    def next_channel(self) -> None:
        channel: int = self.get_channel()
        self.set_channel(channel + 1)
    
    def prev_channel(self) -> None:
        channel: int = self.get_channel()
        self.set_channel(channel - 1)

class SpecialRemote(RemoteControl):
    def __init__(self, tv_factory: TVFactory):
        super().__init__(tv_factory)

    def up(self) -> None:
        channel: int = self.get_channel()
        self.set_channel(channel + 1)

    def down(self) -> None:
        channel: int = self.get_channel()
        self.set_channel(channel - 1)

class Client:
    @staticmethod
    def main(*args) -> None:
        tv_factory: TVFactory = TVFactory()
        remote_sony: RemoteControl = SpecialRemote(tv_factory)
        print("Connect your remote to the Sony TV")
        remote_sony.set_channel("Sony")
        remote_sony.on()
        remote_sony.up()
        remote_sony.down()
        remote_sony.off()

        remote_lg: RemoteControl = GenericRemote(tv_factory)
        print("Connect your remote to the LG TV")
        remote_lg.set_channel("LG")
        remote_lg.on()
        remote_lg.next_channel()
        remote_lg.prev_channel()
        remote_lg.off()

if __name__ == "__main__":
    Client.main()
