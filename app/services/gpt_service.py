import httpx
from app.core.config import settings
from app.schemas.weather import WeatherModel


class GptService:
    def __init__(self):
        self.base_url = 'https://openrouter.ai/api/v1/chat/completions'
        self.api_key = settings.OPEN_ROUTER_API_KEY
    
    async def get_weather_recommendations(self, weather: WeatherModel):
        try:
           weather_info_row = weather
           async with httpx.AsyncClient() as client:
                response = await client.post(
                url=self.base_url,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {self.api_key}'
                },
                json={
                    "model": "microsoft/mai-ds-r1:free",
                    "temperature": 1,
                    "messages": [
                        {
                        "role": "system",
                        "content": "Ты профессиональный метеоконсультант. Анализируй предоставленные JSON-данные о погоде, учитывая все параметры: температура (включая ощущаемую), влажность, скорость ветра, атмосферное давление, облачность, УФ-индекс (рассчитай по времени суток и солнцестоянию), видимость. Сформируй структурированные рекомендации на русском языке по шаблону:\n\n1. **Анализ условий**: краткий вывод о погодных условиях\n2. **Одежда**: подходящий гардероб с учётом thermal comfort\n3. **Активности**: оптимальные виды деятельности на улице\n4. **Здоровье**: предупреждения для метеозависимых людей\n5. **Советы**: дополнительные рекомендации, которые основаны на погдных условиях и месте проживания (например, необходимость солнцезащиты или зонта)\n\nИспользуй единицы измерения СИ. Указывай точные численные значения из данных. Избегай общих фраз — только персонализированные советы. Ответ должен иметь смайлы для большей дружелюбности"
                        },
                        {
                        "role": "user",
                        "content": weather.to_json_str()
                        }
                ]})
                response.raise_for_status()
                data = response.json()
                return data
        except Exception as e:
            print(e)
