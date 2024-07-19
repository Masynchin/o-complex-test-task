from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from corresponse import weather_code_to_icon
from forecast import fetch_forecast


app = FastAPI()
templates = Jinja2Templates(directory="templates")
templates.env.filters["weather_code_to_icon"] = weather_code_to_icon
templates.env.globals["zip"] = zip


@app.get("/")
async def handle_index(request: Request):
    return FileResponse(path="index.html")


@app.get("/forecast", response_class=HTMLResponse)
async def handle_forecast(request: Request, city: str):
    forecast = await fetch_forecast(city)
    return templates.TemplateResponse(
        request=request,
        name="forecast.html",
        context={"city": city, "forecast": forecast},
    )
