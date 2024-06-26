import os

from domain.weather_app import WeatherApp
from domain.weather_observation import create_weather_observation, WeatherObservationRepository, WeatherObservation
from infrastructure.console_adapter import ConsoleAdapter
from infrastructure.csv_export import CsvExporter
from infrastructure.open_meteo_api import OpenMeteoAPI

LIST_OF_TWO_WEATHER_OBSERVATIONS = [
    create_weather_observation(id=1,
                               name='Test',
                               date='2021-01-01',
                               time='12:00',
                               temperature=20.0,
                               pressure=1013.25,
                               wind_direction='N'),
    create_weather_observation(id=2,
                               name='Test 2',
                               date='2021-01-01',
                               time='12:00',
                               temperature=20.0,
                               pressure=1013.25,
                               wind_direction='N')
]


def test_create_weather_observation():
    observation = create_weather_observation(id=1,
                                             name='Test',
                                             date='2021-01-01',
                                             time='12:00',
                                             temperature=20.0,
                                             pressure=1013.25,
                                             wind_direction='N')
    assert observation.id == 1


class InMemoryWeatherObservationRepository(WeatherObservationRepository):
    def get_all_weather_observations(self) -> list[WeatherObservation]:
        return LIST_OF_TWO_WEATHER_OBSERVATIONS


def test_get_weather_observation_from_in_memory_repository():
    repository = InMemoryWeatherObservationRepository()
    observations = repository.get_all_weather_observations()
    assert len(observations) == 2


def test_unit_open_meteo_api():
    open_meteo_api = OpenMeteoAPI()
    observations = open_meteo_api.get_all_weather_observations()
    assert len(observations) > 0
    assert isinstance(observations[0], WeatherObservation)


def test_unit_csv_exporter():
    test_filename = 'test.csv'
    csv_exporter = CsvExporter(test_filename)
    csv_exporter.export(LIST_OF_TWO_WEATHER_OBSERVATIONS)
    assert os.path.exists(test_filename)
    os.remove(test_filename)


def test_integration_end_to_end_open_meteo_api_and_csv_exporter():
    # 1. Instantiate right-side adapter(s) ("I want to go outside the hexagon")
    open_meteo_api = OpenMeteoAPI()
    test_filename = 'test.csv'
    csv_exporter = CsvExporter(test_filename)

    # 2. Instantiate the hexagon
    weather_app = WeatherApp(open_meteo_api, csv_exporter)

    # 3. Instantiate the left-side adapter(s) ("I want ask/to go inside the hexagon")
    console_adapter = ConsoleAdapter(weather_app)
    console_adapter.get_and_export_all_weather_observations()

    # 4. Assert
    assert os.path.exists(test_filename)
    os.remove(test_filename)