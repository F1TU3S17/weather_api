import httpx     
from app.core.config import settings

class OpenWeatherMapService:
    def __init__(self):
        self.base_url = 'https://api.openweathermap.org'
        self.api_key = settings.OPENWEATHER_API_KEY
    
    async def get_city_data(self, city_name: str):
        try:
           async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/geo/1.0/direct",
                    params={
                        "q": city_name,
                        "appid": self.api_key,
                        "limit": 5
                    }
                )
                response.raise_for_status()
                data = response.json()
                return data
        except Exception as e:
            print(e)

    async def get_weather_city(self, lat: float, lon: float):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/data/2.5/weather",
                    params={
                        "lat": lat,
                        'lon': lon,
                        "appid": self.api_key,
                    }
                )
                response.raise_for_status()
                data = response.json()
                return data
        except Exception as e:
            print(e)
