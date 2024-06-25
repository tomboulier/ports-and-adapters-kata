import json
import requests
from domain.weather_observation import WeatherObservationRepository, WeatherObservation


class OpenMeteoAPI(WeatherObservationRepository):

    def __init__(self):
        self.url = ("https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2024-06"
                    "-09&end_date=2024-06-23&hourly=temperature_2m,surface_pressure,wind_direction_100m")

    def get_all_weather_observations(self) -> list[WeatherObservation]:
        response = requests.get(self.url)
        return json.loads(response.content)