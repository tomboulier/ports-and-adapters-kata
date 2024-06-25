from domain.weather_observation import create_weather_observation


def test_create_weather_observation():
    observation = create_weather_observation(id=1,
                                     name='Test',
                                     date='2021-01-01',
                                     time='12:00',
                                     temperature=20.0,
                                     pressure=1013.25,
                                     wind_direction='N')
