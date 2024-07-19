import pandas as pd

from app.exceptions import CityNotFound


df = pd.read_csv("towns.csv")

def city_geocords(city: str) -> (float, float):
    matches = df[df["city"].str.match(city, case=False)]
    if len(matches) != 1:
        raise CityNotFound(city)
    else:
        match = matches.iloc[0]
        lat = float(match["lat"])
        lon = float(match["lon"])
        return (lat, lon)


def city_suggestions(part: str) -> list[str]:
    return list(df[df["city"].str.contains(part, case=False)]["city"])
