from abc import ABC, abstractmethod
from typing import List
from domain.weather_observation import WeatherObservation


class DataExporter(ABC):
    @abstractmethod
    def export(self, data: List[WeatherObservation]):
        pass
