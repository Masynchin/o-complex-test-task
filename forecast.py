from datetime import datetime

from aiohttp import ClientSession
from pydantic import BaseModel


class CurrentUnits(BaseModel):
    time: str
    interval: str
    temperature_2m: str
    relative_humidity_2m: str
    apparent_temperature: str
    is_day: str
    precipitation: str
    rain: str
    showers: str
    snowfall: str
    weather_code: str
    cloud_cover: str
    surface_pressure: str
    wind_speed_10m: str
    wind_direction_10m: str
    wind_gusts_10m: str


class Current(BaseModel):
    time: datetime
    interval: int
    temperature_2m: float
    relative_humidity_2m: int
    apparent_temperature: float
    is_day: int
    precipitation: float
    rain: float
    showers: float
    snowfall: float
    weather_code: int
    cloud_cover: int
    surface_pressure: float
    wind_speed_10m: float
    wind_direction_10m: int
    wind_gusts_10m: float


class HourlyUnits(BaseModel):
    time: str
    temperature_2m: str
    precipitation: str
    weather_code: str


class Hourly(BaseModel):
    time: list[datetime]
    temperature_2m: list[float]
    precipitation: list[float]
    weather_code: list[int]


class CurrentForecast(BaseModel):
    latitude: float
    longitude: float
    generationtime_ms: float
    utc_offset_seconds: int
    timezone: str
    timezone_abbreviation: str
    elevation: float
    current_units: CurrentUnits
    current: Current
    hourly_units: HourlyUnits
    hourly: Hourly


def city_geocords(city: str) -> (float, float):
    return (59.1333, 37.9)


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
