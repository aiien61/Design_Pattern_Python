from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, *args, **kwargs): raise NotImplementedError


class Observable(ABC):
    def __init__(self) -> None:
        self.observers: List[Observer] = []

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    @abstractmethod
    def notify_observers(self): raise NotImplementedError

class DisplayElement(ABC):
    @abstractmethod
    def display(self): raise NotImplementedError


class WeatherData(Observable):
    __temperature: float
    __humidity: float
    __pressure: float

    def __init__(self):
        super().__init__()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def set_measurements(self, temperaute: float, humidity: float, pressure: float) -> None:
        self.__temperature: float = temperaute
        self.__humidity: float = humidity
        self.__pressure: float = pressure
        self.measurements_changed()

    def measurements_changed(self) -> None:
        self.notify_observers()

    def get_temperature(self) -> float:
        return self.__temperature
    
    def get_humidity(self) -> float:
        return self.__humidity
    
    def get_pressure(self) -> float:
        return self.__pressure
    

class CurrentConditionsDisplay(Observer, DisplayElement):
    __temperature: float
    __humidity: float

    def __init__(self, observable: Observable):
        observable.register_observer(self)

    def subscribe(self, observable: Observable) -> bool:
        observable.register_observer(self)
        return True

    def unsubscribe(self, observable: Observable) -> bool:
        observable.remove_observer(self)
        return True

    def update(self, observable: Observable):
        if isinstance(observable, WeatherData):
            weather_data: WeatherData = observable
            self.__temperature = weather_data.get_temperature()
            self.__humidity = weather_data.get_humidity()
        self.display()

    def display(self) -> None:
        print(f"Current conditions: {self.__temperature}F degrees\
              \n                    {self.__humidity}% humidity")


class StatisticsDisplay(Observer, DisplayElement):
    __max_temp: float = 0.0
    __min_temp: float = 200.0
    __temp_sum: float = 0.0
    __num_readings: int = 0

    def __init__(self, observable: Observable) -> None:
        observable.register_observer(self)

    def subscribe(self, observable: Observable) -> bool:
        observable.register_observer(self)
        return True

    def unsubscribe(self, observable: Observable) -> bool:
        observable.remove_observer(self)
        return True

    def update(self, observable: Observable) -> None:
        if isinstance(observable, WeatherData):
            weather_data: WeatherData = observable
            temperature: float = weather_data.get_temperature()
            self.__temp_sum += temperature
            self.__num_readings += 1

            if temperature > self.__max_temp:
                self.__max_temp = temperature
            
            if temperature < self.__min_temp:
                self.__min_temp = temperature
            
        self.display()

    def display(self) -> None:
        print(f"Weather Statistics: Avg temperature: {self.__temp_sum/self.__num_readings}\
              \n                    Max temperature: {self.__max_temp}\
              \n                    Min temperature: {self.__min_temp}")


class ForecastDisplay(Observer, DisplayElement):
    __current_pressure: float = 29.92
    __last_pressure: float

    def __init__(self, observable: Observable) -> None:
        observable.register_observer(self)

    def subscribe(self, observable: Observable) -> bool:
        observable.register_observer(self)
        return True

    def unsubscribe(self, observable: Observable) -> bool:
        observable.remove_observer(self)
        return True

    def update(self, observable: Observable) -> None:
        if isinstance(observable, WeatherData):
            weather_data: WeatherData = observable
            self.__last_pressure = self.__current_pressure
            self.__current_pressure = weather_data.get_pressure()
        self.display()

    def display(self) -> None:
        print('Forecast: ', end='')
        if self.__current_pressure > self.__last_pressure:
            print('Improving weather on the way!')
        elif self.__current_pressure == self.__last_pressure:
            print('More of the same')
        elif self.__current_pressure < self.__last_pressure:
            print('Watch out for cooler, rainy weather')
    

class HeatIndexDisplay(Observer, DisplayElement):
    __heat_index: float = 0.0

    def __init__(self, observable: Observable):
        observable.register_observer(self)
    
    def subscribe(self, observable: Observable) -> bool:
        observable.register_observer(self)
        return True

    def unsubscribe(self, observable: Observable) -> bool:
        observable.remove_observer(self)
        return True
    
    def update(self, observable: Observable) -> None:
        if isinstance(observable, WeatherData):
            weather_data: WeatherData = observable
            t: float = weather_data.get_temperature()
            rh: float = weather_data.get_humidity()
            self.__heat_index = float(
                (16.923 + (0.185212 * t)) +
                (5.37941 * rh) -
                (0.100254 * t * rh) +
                (0.00941695 * (t * t)) +
                (0.00728898 * (rh * rh)) +
                (0.000345372 * (t * t * rh)) -
                (0.000814971 * (t * rh * rh)) +
                (0.0000102102 * (t * t * rh * rh)) -
                (0.000038646 * (t * t * t)) +
                (0.0000291583 * (rh * rh * rh)) +
                (0.00000142721 * (t * t * t * rh)) +
                (0.000000197483 * (t * rh * rh * rh)) -
                (0.0000000218429 * (t * t * t * rh * rh)) +
                (0.000000000843296 * (t * t * rh * rh * rh)) -
                (0.0000000000481975 * (t * t * t * rh * rh * rh))
            )
        self.display()

    def display(self) -> None:
        print(f'Heat index is {self.__heat_index:.2f}')


class WeatherStation:
    @staticmethod
    def main(*args) -> None:
        weather_data: WeatherData = WeatherData()
        
        current_conditions: CurrentConditionsDisplay = CurrentConditionsDisplay(weather_data)
        statistics_display: StatisticsDisplay = StatisticsDisplay(weather_data)
        forecast_display: ForecastDisplay = ForecastDisplay(weather_data)

        print(f'\nWeahter changes! temperature -> 80, humidity -> 65, pressure -> 30.4')
        weather_data.set_measurements(80.0, 65.0, 30.4)
        print(f'\nWeahter changes! temperature -> 82, humidity -> 70, pressure -> 29.2')
        weather_data.set_measurements(82.0, 70.0, 29.2)
        print(f'\nWeahter changes! temperature -> 78, humidity -> 90, pressure -> 29.2')
        weather_data.set_measurements(78.0, 90.0, 29.2)

        print('\nforecast_display unsubscribes weather_data notification', end=' ')
        print(forecast_display.unsubscribe(weather_data))

        print('Initialise heatindex_display and subscribes weather_data notification')
        heatindex_display: HeatIndexDisplay = HeatIndexDisplay(weather_data)
        
        print(f'\nWeahter changes! temperature -> 62, humidity -> 90, pressure -> 29.2')
        weather_data.set_measurements(62, 90, 29.2)

        print('\nforecast_display subscribes weather_data notification again', end=' ')
        print(forecast_display.subscribe(weather_data))
        print('heatindex_display unsubscribes weather_data notification', end=' ')
        print(heatindex_display.unsubscribe(weather_data))

        print(f'\nWeahter changes! temperature -> 80, humidity -> 70, pressure -> 29.2')
        weather_data.set_measurements(80, 70, 29.2)

if __name__ == '__main__':
    WeatherStation.main()