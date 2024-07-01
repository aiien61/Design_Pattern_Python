from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        raise NotImplementedError


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer): raise NotImplementedError

    @abstractmethod
    def remove_observer(self, observer: Observer): raise NotImplementedError

    @abstractmethod
    def notify_observers(self): raise NotImplementedError

class DisplayElement(ABC):
    @abstractmethod
    def display(self): raise NotImplementedError


class WeatherData(Subject):
    _observers: List[Observer]
    _temperature: float
    _humidity: float
    _pressure: float

    def __init__(self):
        self._observers: List[Observer] = []
    
    def register_observer(self, observer: Observer) -> bool:
        self._observers.append(observer)
        return True

    def remove_observer(self, observer: Observer) -> bool:
        self._observers.remove(observer)
        return True

    def notify_observers(self) -> bool:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)
        return True
    
    def measurements_changed(self) -> None:
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> True:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.measurement_changed()

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, observable: Subject):
        self._temperature = None
        self._humidity = None
        self._pressure = None
        self._observable = observable
        observable.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.display()
    
    def display(self) -> None:
        print(f'Current conditions: {self._temperature:.1f}F degrees\
              \n                    {self._humidity:.1f}% humidity')
        return None

class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, observable: Subject):
        self._max_temp: float = 0.0
        self._min_temp: float = 200
        self._temp_sum: float = 0.0
        self._num_readings: int = 0
        self._observable = observable
        observable.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temp_sum += temperature
        self._num_readings += 1

        if temperature > self._max_temp:
            self._max_temp = temperature
        if temperature < self._min_temp:
            self._min_temp = temperature
        
        self.display()

    def display(self) -> None:
        print(f"Weather Statistics: Avg temperature: {self._temp_sum/self._num_readings}\
              \n                    Max temperature: {self._max_temp}\
              \n                    Min temperature: {self._min_temp}")

class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, observable: Subject):
        self._current_pressure = 29.92
        self._last_pressure = None
        self._observable = observable
        observable.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self._last_pressure = self._current_pressure
        self._current_pressure = pressure
        self.display()

    def display(self):
        print('Forecast: ', end='')
        if self._current_pressure > self._last_pressure:
            print('Improving weather on the way!')
        elif self._current_pressure == self._last_pressure:
            print('More of the same')
        elif self._current_pressure < self._last_pressure:
            print('Watch out for cooler, rainy weather')


def weather_station():
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    print(f'Weahter changes! temperature -> 80, humidity -> 65, pressure -> 30.5')
    weather_data.set_measurements(80, 65, 30.5)

    print(f'Weahter changes! temperature -> 82, humidity -> 70, pressure -> 29.2')
    weather_data.set_measurements(82, 70, 29.2)

    print(f'Weahter changes! temperature -> 78, humidity -> 90, pressure -> 30.5')
    weather_data.set_measurements(78, 90, 30.5)

    weather_data.remove_observer(forecast_display)

    print(f'Weahter changes! temperature -> 62, humidity -> 90, pressure -> 29.2')
    weather_data.set_measurements(62, 90, 29.2)

if __name__ == '__main__':
    weather_station()