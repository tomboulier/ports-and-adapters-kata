from abc import ABC, abstractmethod

from domain.weather_observation import WeatherObservationRepository
from domain.data_export import DataExporter


class WeatherAppFacade(ABC):
    @abstractmethod
    def get_and_export_all_weather_observations(self):
        pass


class WeatherApp(WeatherAppFacade):
    def get_and_export_all_weather_observations(self):
        weather_observations = self.weather_observation_repository.get_all_weather_observations()
        self.data_exporter.export(weather_observations)

    def __init__(self, weather_observation_repository: WeatherObservationRepository, data_exporter: DataExporter):
        self.weather_observation_repository = weather_observation_repository
        self.data_exporter = data_exporter
