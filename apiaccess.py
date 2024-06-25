import requests, json

url = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date=2024-06-09&end_date=2024-06-23&hourly=temperature_2m,surface_pressure,wind_direction_100m"
response = requests.get(url)
print(json.loads(response.content))