from domain.weather_observation import create_weather_observation, WeatherObservationRepository, WeatherObservation
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
