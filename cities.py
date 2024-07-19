import pandas as pd

from exceptions import CityNotFound


df = pd.read_csv("towns.csv")

def city_geocords(city: str) -> (float, float):
    matches = df[df["city"].str.match(city)]
    if len(matches) != 1:
        raise CityNotFound(city)
    else:
        match = matches.iloc[0]
        lat = float(match["lat"])
        lon = float(match["lon"])
        return (lat, lon)
