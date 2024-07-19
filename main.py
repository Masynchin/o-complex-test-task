from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from forecast import fetch_forecast


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def handle_index(request: Request):
    return FileResponse(path="index.html")


@app.get("/forecast/{city}", response_class=HTMLResponse)
async def handle_forecast(request: Request, city: str):
    forecast = await fetch_forecast(city)
    return templates.TemplateResponse(
        request=request, name="forecast.html", context={"forecast": forecast}
    )