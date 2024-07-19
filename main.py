from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from app.cities import city_suggestions
from app.exceptions import CityNotFound
from app.forecast import fetch_forecast


app = FastAPI()
templates = Jinja2Templates(directory="templates")
templates.env.globals["zip"] = zip


@app.get("/")
async def handle_index(request: Request):
    return FileResponse(path="index.html")


@app.get("/forecast", response_class=HTMLResponse)
async def handle_forecast(request: Request, city: str):
    try:
        forecast = await fetch_forecast(city)
        return templates.TemplateResponse(
            request=request,
            name="forecast.html",
            context={"city": city, "forecast": forecast},
        )
    except CityNotFound as e:
        return templates.TemplateResponse(
            request=request, name="city_not_found.html", context={"city": e.city}
        )


@app.get("/suggestions", response_class=HTMLResponse)
async def handle_suggestions(request: Request, city: str):
    suggestions = city_suggestions(city)[:10]
    return templates.TemplateResponse(
        request=request, name="suggestions.html", context={"suggestions": suggestions},
    )
