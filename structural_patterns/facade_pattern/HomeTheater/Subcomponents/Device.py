from abc import ABC, abstractmethod


class AudioDevice(ABC):
    @abstractmethod
    def on(self): raise NotImplementedError

    @abstractmethod
    def off(self): raise NotImplementedError

    @abstractmethod
    def set_volume(self): raise NotImplementedError


class RadioDevice(ABC):
    @abstractmethod
    def on(self): raise NotImplementedError

    @abstractmethod
    def off(self): raise NotImplementedError


class PlayerDevice(ABC):
    @abstractmethod
    def on(self): raise NotImplementedError

    @abstractmethod
    def off(self): raise NotImplementedError

    @abstractmethod
    def play(self): raise NotImplementedError


class VisualDevice(ABC):
    @abstractmethod
    def on(self): raise NotImplementedError

    @abstractmethod
    def off(self): raise NotImplementedError



class LightingDevice(ABC):
    @abstractmethod
    def on(self): raise NotImplementedError

    @abstractmethod
    def off(self): raise NotImplementedError
