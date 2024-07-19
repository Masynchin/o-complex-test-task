def weather_code_to_icon(code: int) -> str:
    if code == 3:
        return "day-sunny-overcast"
    else:
        return "day-cloudy"
