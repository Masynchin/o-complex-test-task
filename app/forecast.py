from aiohttp import ClientSession

from app.cities import city_geocords
from app.schema import CurrentForecast


def url_params(geocords: (float, float)) -> str:
    (latitude, longtitude) = geocords
    return {"latitude": latitude, "longitude": longtitude, **default_url_params}


default_url_params = {
    "current": [
        "temperature_2m",
        "relative_humidity_2m",
        "apparent_temperature",
        "is_day",
        "precipitation",
        "rain",
        "showers",
        "snowfall",
        "weather_code",
        "cloud_cover",
        "surface_pressure",
        "wind_speed_10m",
        "wind_direction_10m",
        "wind_gusts_10m",
    ],
    "hourly": ["temperature_2m", "precipitation", "weather_code"],
    "wind_speed_unit": "ms",
    "timezone": "Europe/Moscow",
    "forecast_days": 1,
    "forecast_hours": 8,
}


async def fetch_forecast(city: str) -> CurrentForecast:
    geocords = city_geocords(city)
    params = url_params(geocords)
    async with ClientSession() as session:
        async with session.get(
            "https://api.open-meteo.com/v1/forecast", params=params
        ) as response:
            data = await response.json()
            data = CurrentForecast(**data)
            return data
