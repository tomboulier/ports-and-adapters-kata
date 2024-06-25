import json

import requests
from dataclasses import dataclass

from domain.weather_observation import WeatherObservationRepository, create_weather_observation, WeatherObservation


class OpenMeteoAPI(WeatherObservationRepository):

    def __init__(self):
        self.station_name = "Grenoble"
        self.url = ("https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2024-06"
                    "-09&end_date=2024-06-23&hourly=temperature_2m,surface_pressure,wind_direction_100m")

    def get_all_weather_observations(self) -> list[WeatherObservation]:
        raw_observations = self.fetch_data()

        return self.transform_raw_observations(raw_observations)

    def transform_raw_observations(self, raw_observations) -> list[WeatherObservation]:
        number_of_observations = len(raw_observations)
        weather_observations_list = []
        for index in range(number_of_observations):
            observation = create_weather_observation(id=index,
                                                     name=self.station_name,
                                                     date=raw_observations['time'][index][:10],
                                                     time=raw_observations['time'][index][11:],
                                                     temperature=raw_observations['temperature_2m'][index],
                                                     pressure=raw_observations['surface_pressure'][index],
                                                     wind_direction=raw_observations['wind_direction_100m'][index])
            weather_observations_list.append(observation)
        return weather_observations_list

    def fetch_data(self) -> dict:
        response = requests.get(self.url)
        response_dict = json.loads(response.content)
        raw_observations = response_dict['hourly']
        return raw_observations
