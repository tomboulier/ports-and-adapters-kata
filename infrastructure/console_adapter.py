from domain.weather_app import WeatherAppFacade


class ConsoleAdapter(WeatherAppFacade):
    def get_and_export_all_weather_observations(self) -> None:
        self.weather_app.get_and_export_all_weather_observations()

    def __init__(self, weather_app: WeatherAppFacade):
        self.weather_app = weather_app

