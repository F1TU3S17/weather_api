from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Coord(BaseModel):
    lon: float
    lat: float

class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str

class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: Optional[int] = None
    grnd_level: Optional[int] = None

class Wind(BaseModel):
    speed: float
    deg: int

class Clouds(BaseModel):
    all: int

class Sys(BaseModel):
    type: Optional[int] = None  
    id: Optional[int] = None    
    country: Optional[str] = None
    sunrise: Optional[datetime] = None
    sunset: Optional[datetime] = None

class WeatherModel(BaseModel):
    coord: Coord
    weather: List[Weather]
    base: str
    main: Main
    visibility: int
    wind: Wind
    clouds: Clouds
    dt: datetime
    sys: Optional[Sys] = None 
    timezone: int
    id: int
    name: str
    cod: int

    def to_json_str(self) -> str:
        json_model = self.model_dump_json(indent=2, exclude_none=True)
        str_model = str(json_model)
        return str_model
