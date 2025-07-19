# 🌤️ Weather Service API

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com/)

Современный REST API для получения актуальной погодной информации с интеллектуальными рекомендациями на основе ИИ. Проект построен на FastAPI с использованием Redis для кэширования и интегрирован с OpenWeatherMap API и OpenRouter AI.

API доступен - https://weather-api-9ie8.onrender.com/

## ✨ Возможности

- 🏙️ **Поиск городов** - Найдите координаты любого города мира с поддержкой множественных результатов
- 🌡️ **Погодные данные** - Получите подробную информацию о текущей погоде: температура, влажность, ветер и многое другое
- 🤖 **ИИ рекомендации** - Персонализированные советы по одежде, активностям и здоровью на основе погодных условий
- ⚡ **Redis кэширование** - Быстрые ответы благодаря интеллектуальному кэшированию данных
- 🐳 **Docker поддержка** - Простой запуск с помощью Docker и Docker Compose
- 📚 **Автоматическая документация** - Swagger UI и ReDoc интерфейсы
- 🚀 **Высокая производительность** - Асинхронная архитектура с FastAPI

## 🛠️ Технологии

- **Framework**: FastAPI 0.116.1
- **Language**: Python 3.11+
- **Cache**: Redis 6.2.0
- **HTTP Client**: httpx 0.28.1
- **Validation**: Pydantic 2.11.7
- **ASGI Server**: Uvicorn 0.35.0
- **Containerization**: Docker & Docker Compose

## 📋 Предварительные требования

- Python 3.11 или выше
- Redis (или используйте Docker Compose)
- API ключ от [OpenWeatherMap](https://openweathermap.org/api)
- API ключ от [OpenRouter](https://openrouter.ai/) для ИИ рекомендаций

## 🚀 Быстрый старт

### Способ 1: Docker Compose (рекомендуется)

1. **Клонируйте репозиторий**
   ```bash
   git clone url
   ```

2. **Настройте переменные окружения**
   ```bash
   cp .env.example .env
   # Отредактируйте .env файл и добавьте ваши API ключи
   ```

3. **Запустите с Docker Compose**
   ```bash
   docker-compose up -d
   ```

4. **Откройте браузер**
   - API: http://localhost:8000
   - Документация: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Способ 2: Локальная установка

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/F1TU3S17/weather_api.git
   cd weather_api
   ```

2. **Создайте виртуальное окружение**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте переменные окружения**
   ```bash
   cp .env.example .env
   # Отредактируйте .env файл
   ```

5. **Запустите Redis** (если не используете Docker)
   ```bash
   redis-server
   ```

6. **Запустите приложение**
   ```bash
   python main.py
   # или
   uvicorn main:app --reload
   ```

## ⚙️ Настройка переменных окружения

Создайте файл `.env` на основе `.env.example`:

```env
# OpenWeatherMap API ключ
OPENWEATHER_API_KEY=your_openweather_api_key_here

# OpenRouter API ключ для GPT
OPEN_ROUTER_API_KEY=your_openrouter_api_key_here

# URL для подключения к Redis
LOCAL_REDIS_URL=redis://redis:6379/0  # для Docker
# LOCAL_REDIS_URL=redis://localhost:6379/0  # для локального запуска
```

## 📡 API Endpoints

### 🏙️ Города

#### Поиск города
```http
GET /api/v1/city/{city_name}
```

**Пример запроса:**
```bash
curl -X GET "http://localhost:8000/api/v1/city/Moscow"
```

**Пример ответа:**
```json
[
  {
    "name": "Moscow",
    "lat": 55.7522,
    "lon": 37.6156,
    "country": "RU",
    "state": null
  }
]
```

### 🌡️ Погода

#### Получить текущую погоду
```http
POST /api/v1/weather/
```

**Тело запроса:**
```json
{
  "lat": 55.7522,
  "lon": 37.6156
}
```

**Пример ответа:**
```json
{
  "coord": {
    "lon": 37.6156,
    "lat": 55.7522
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "main": {
    "temp": 273.15,
    "feels_like": 269.15,
    "temp_min": 271.15,
    "temp_max": 275.15,
    "pressure": 1013,
    "humidity": 65
  },
  "visibility": 10000,
  "wind": {
    "speed": 3.5,
    "deg": 180
  },
  "clouds": {
    "all": 0
  },
  "name": "Moscow"
}
```

#### Получить ИИ рекомендации
```http
POST /api/v1/weather/recomendation
```

**Тело запроса:** Объект WeatherModel (полученный из предыдущего запроса)

**Пример ответа:**
```json
{
  "content": "🌤️ **Анализ условий**: Отличная ясная погода...",
  "reasoning": "Анализ погодных условий показывает..."
}
```

## 🏗️ Архитектура проекта

```
weather_api/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           ├── city.py          # Эндпоинты для работы с городами
│   │           └── weather.py       # Эндпоинты для работы с погодой
│   ├── core/
│   │   ├── config.py               # Настройки приложения
│   │   └── html/
│   │       └── root_html.py        # HTML главной страницы
│   ├── schemas/
│   │   ├── city.py                 # Pydantic модели для городов
│   │   ├── gpt.py                  # Модели для ИИ ответов
│   │   └── weather.py              # Модели для погодных данных
│   └── services/
│       ├── gpt_service.py          # Сервис для работы с ИИ
│       └── open_weather_map_service.py  # Сервис OpenWeatherMap
├── docker-compose.yml              # Docker Compose конфигурация
├── Dockerfile                      # Docker образ
├── main.py                         # Точка входа приложения
├── requirements.txt                # Python зависимости
└── .env.example                    # Пример переменных окружения
```

## 🔄 Кэширование

Проект использует Redis для кэширования ответов API:

- **Данные о городах**: кэшируются на 30 минут (1800 секунд)
- **Погодные данные**: кэшируются на 30 минут (1800 секунд)
- **ИИ рекомендации**: кэшируются на 1 минуту (60 секунд)

## 🐳 Docker

### Сборка образа
```bash
docker build -t weather-api .
```

### Запуск с Docker Compose
```bash
docker-compose up -d
```

### Остановка
```bash
docker-compose down
```

## 📊 Мониторинг и логи

### Просмотр логов
```bash
# Все сервисы
docker-compose logs -f

# Только приложение
docker-compose logs -f app

# Только Redis
docker-compose logs -f redis
```

### Проверка статуса
```bash
docker-compose ps
```

## 👤 Автор

**F1TU3S17**

- GitHub: [@F1TU3S17](https://github.com/F1TU3S17)

⭐ Поставьте звезду, если проект был полезен!
