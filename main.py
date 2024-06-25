# 1. Instantiate right-side adapter(s) ("I want to go outside the hexagon")
from domain.weather_app import WeatherApp
from infrastructure.console_adapter import ConsoleAdapter
from infrastructure.csv_export import CsvExporter
from infrastructure.open_meteo_api import OpenMeteoAPI

if __name__ == '__main__':
    # 1. Instantiate right-side adapter(s) ("I want to go outside the hexagon")
    open_meteo_api = OpenMeteoAPI()
    test_filename = 'weather_observations.csv'
    csv_exporter = CsvExporter(test_filename)

    # 2. Instantiate the hexagon
    weather_app = WeatherApp(open_meteo_api, csv_exporter)

    # 3. Instantiate the left-side adapter(s) ("I want ask/to go inside the hexagon")
    console_adapter = ConsoleAdapter(weather_app)
    console_adapter.get_and_export_all_weather_observations()