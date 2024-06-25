from dataclasses import dataclass


@dataclass
class WeatherObservation:
    id: int
    name: str
    date: str
    time: str
    temperature: float
    pressure: float
    wind_direction: str
