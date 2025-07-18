from typing import List
from fastapi import APIRouter
from app.schemas.city import CityModel
from app.services.open_weather_map_service import OpenWeatherMapService
from fastapi_cache.decorator import cache

router = APIRouter(prefix="/city", tags=["City"])

@router.get("/{city}", response_model=List[CityModel])

@cache(expire=1800)
async def get_city_data(city: str):
    weather_service = OpenWeatherMapService()
    data = await weather_service.get_city_data(city)
    city_list = []
    for i in range(len(data)):
        cityModel = CityModel(
            name=data[i]['name'], 
            lat=data[i]['lat'], 
            lon=data[i]['lon'],
            country=data[i]['country'],
            state=data[i]['state']
        )
        city_list.append(cityModel)
    return city_list