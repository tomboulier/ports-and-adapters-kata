from domain.data_export import DataExporter
from domain.weather_observation import WeatherObservation


class CsvExporter(DataExporter):
    def __init__(self, filename: str):
        self.filename = filename

    def export(self, data: list[WeatherObservation]):
        with open(self.filename, 'w') as file:
            file.write('id,name,date,time,temperature,pressure,wind_direction\n')
            for observation in data:
                file.write(f'{observation.id},{observation.name},{observation.date},{observation.time},'
                           f'{observation.temperature},{observation.pressure},{observation.wind_direction}\n')
