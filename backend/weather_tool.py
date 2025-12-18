import os
import requests

def get_weather(city: str) -> str:
    """Get real weather data"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key or api_key == "demo":
        return f"Weather in {city}: 28°C, clear sky (get free API key at openweathermap.org)"
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if response.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"{desc}, {temp}°C"
        return f"City '{city}' not found"
    except Exception as e:
        return f"Weather service unavailable"
