from typing import AsyncIterator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.api.v1.endpoints import weather
from app.api.v1.endpoints import city
from app.core.config import settings

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url(settings.LOCAL_REDIS_URL)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(title="Weather Service", version="1.0.0",lifespan=lifespan)
# Регистрация роутеров
app.include_router(weather.router, prefix="/api/v1")
app.include_router(city.router, prefix="/api/v1" )

@app.get("/", response_class=HTMLResponse)
async def root():
    html_data = "<h1>Welcome to Weather Service!</h1>"
    return HTMLResponse(content=html_data)


if __name__ == "__main__": 
    import uvicorn
    uvicorn.run(app)