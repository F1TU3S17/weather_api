from fastapi import APIRouter, Depends

from app.schemas.gpt import GptMessage
from app.services.gpt_service import GptService
from app.schemas.weather import Coord, WeatherModel
from app.services.open_weather_map_service import OpenWeatherMapService

from fastapi_cache.decorator import cache

router = APIRouter(prefix="/weather", tags=["Weather"])

@cache(expire=1800)
@router.post('/', response_model=WeatherModel)
async def get_current_weather(coord: Coord):
    weather_service = OpenWeatherMapService()
    data = await weather_service.get_weather_city(lat=coord.lat, lon=coord.lon)
    weather = WeatherModel(**data)
    return weather

@cache(expire=60)
@router.post('/recomendation')
async def get_recomendation(weather: WeatherModel):
    gpt_service = GptService()
    data = await gpt_service.get_weather_recommendations(weather=weather)
    message_data = data['choices'][0]['message']
    message = GptMessage(content=message_data['content'], reasoning=message_data['reasoning'])
    return message
