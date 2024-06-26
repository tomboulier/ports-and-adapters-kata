from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class WeatherObservation:
    id: int
    name: str
    date: str
    time: str
    temperature: float
    pressure: float
    wind_direction: str


def create_weather_observation(id: int,
                               name: str,
                               date: str,
                               time: str,
                               temperature: float,
                               pressure: float,
                               wind_direction: str
                               ) -> WeatherObservation:
    return WeatherObservation(id=id,
                              name=name,
                              date=date,
                              time=time,
                              temperature=temperature,
                              pressure=pressure,
                              wind_direction=wind_direction)


class WeatherObservationRepository(ABC):
    @abstractmethod
    def get_all_weather_observations(self) -> list[WeatherObservation]:
        pass
