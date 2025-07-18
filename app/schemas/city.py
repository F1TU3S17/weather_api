from pydantic import BaseModel

class CityModel(BaseModel):
    name: str
    lat: float
    lon: float
    country: str
    state: str

