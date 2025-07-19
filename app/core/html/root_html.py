html_data = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Weather Service API</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            
            .container {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 40px;
                max-width: 800px;
                width: 100%;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            
            .logo {
                font-size: 4rem;
                margin-bottom: 20px;
                background: linear-gradient(45deg, #667eea, #764ba2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            
            h1 {
                color: #333;
                font-size: 2.5rem;
                margin-bottom: 15px;
                font-weight: 700;
            }
            
            .subtitle {
                color: #666;
                font-size: 1.2rem;
                margin-bottom: 30px;
                line-height: 1.6;
            }
            
            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin: 40px 0;
            }
            
            .feature {
                background: #f8f9fa;
                padding: 25px;
                border-radius: 15px;
                border-left: 4px solid #667eea;
                transition: transform 0.3s ease;
            }
            
            .feature:hover {
                transform: translateY(-5px);
            }
            
            .feature-icon {
                font-size: 2rem;
                margin-bottom: 10px;
            }
            
            .feature h3 {
                color: #333;
                margin-bottom: 10px;
                font-size: 1.2rem;
            }
            
            .feature p {
                color: #666;
                line-height: 1.5;
            }
            
            .buttons {
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 40px;
            }
            
            .btn {
                display: inline-flex;
                align-items: center;
                gap: 10px;
                padding: 15px 30px;
                text-decoration: none;
                border-radius: 50px;
                font-weight: 600;
                font-size: 1.1rem;
                transition: all 0.3s ease;
                border: 2px solid;
            }
            
            .btn-primary {
                background: linear-gradient(45deg, #667eea, #764ba2);
                color: white;
                border-color: transparent;
            }
            
            .btn-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
            }
            
            .btn-secondary {
                background: transparent;
                color: #667eea;
                border-color: #667eea;
            }
            
            .btn-secondary:hover {
                background: #667eea;
                color: white;
                transform: translateY(-2px);
            }
            
            .api-info {
                background: #e3f2fd;
                border-radius: 15px;
                padding: 25px;
                margin: 30px 0;
                border-left: 4px solid #2196f3;
            }
            
            .api-info h3 {
                color: #1976d2;
                margin-bottom: 15px;
            }
            
            .endpoints {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin-top: 20px;
            }
            
            .endpoint {
                background: white;
                padding: 15px;
                border-radius: 10px;
                font-family: 'Courier New', monospace;
                font-size: 0.9rem;
                color: #333;
            }
            
            .method {
                font-weight: bold;
                color: #4caf50;
            }
            
            .footer {
                margin-top: 40px;
                padding-top: 20px;
                border-top: 1px solid #eee;
                color: #999;
                font-size: 0.9rem;
            }
            
            @media (max-width: 768px) {
                .container {
                    padding: 30px 20px;
                    margin: 10px;
                }
                
                .logo {
                    font-size: 3rem;
                }
                
                h1 {
                    font-size: 2rem;
                }
                
                .buttons {
                    flex-direction: column;
                    align-items: center;
                }
                
                .btn {
                    width: 100%;
                    max-width: 300px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">🌤️</div>
            <h1>Weather Service API</h1>
            <p class="subtitle">
                Современный REST API для получения актуальной погодной информации 
                с интеллектуальными рекомендациями на основе ИИ
            </p>
            
            <div class="features">
                <div class="feature">
                    <div class="feature-icon">🏙️</div>
                    <h3>Поиск городов</h3>
                    <p>Найдите координаты любого города мира с поддержкой множественных результатов</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">🌡️</div>
                    <h3>Погодные данные</h3>
                    <p>Получите подробную информацию о текущей погоде: температура, влажность, ветер и многое другое</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">🤖</div>
                    <h3>ИИ рекомендации</h3>
                    <p>Персонализированные советы по одежде, активностям и здоровью на основе погодных условий</p>
                </div>
                <div class="feature">
                    <div class="feature-icon">⚡</div>
                    <h3>Redis кэширование</h3>
                    <p>Быстрые ответы благодаря интеллектуальному кэшированию данных</p>
                </div>
            </div>
            
            <div class="api-info">
                <h3>📡 Доступные эндпоинты</h3>
                <div class="endpoints">
                    <div class="endpoint">
                        <span class="method">GET</span> /api/v1/city/{city}
                    </div>
                    <div class="endpoint">
                        <span class="method">POST</span> /api/v1/weather/
                    </div>
                    <div class="endpoint">
                        <span class="method">POST</span> /api/v1/weather/recomendation
                    </div>
                </div>
            </div>
            
            <div class="buttons">
                <a href="/docs" class="btn btn-primary">
                    📚 Документация API
                </a>
                <a href="/redoc" class="btn btn-secondary">
                    📖 ReDoc
                </a>
            </div>
            
            <div class="footer">
                <p>Powered by FastAPI • OpenWeatherMap • OpenRouter AI</p>
                <p>© 2025 Weather Service. Версия 1.0.0</p>
            </div>
        </div>
    </body>
    </html>
    """