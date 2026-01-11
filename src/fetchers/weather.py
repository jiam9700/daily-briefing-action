from typing import Dict, Any, Optional
from src.config import Config
from src.utils.retry import get_retry_session

def fetch_weather() -> Optional[Dict[str, Any]]:
    """
    Fetches weather data from Open-Meteo for Melbourne.
    No API Key required.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": Config.LATITUDE,
        "longitude": Config.LONGITUDE,
        "current": "temperature_2m,weather_code",
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "Australia/Melbourne"
    }

    session = get_retry_session()
    
    try:
        response = session.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        current = data.get("current", {})
        daily = data.get("daily", {})
        
        return {
            "current_temp": current.get("temperature_2m"),
            "max_temp": daily.get("temperature_2m_max", [None])[0],
            "min_temp": daily.get("temperature_2m_min", [None])[0],
            "weather_code": current.get("weather_code")
        }
        
    except Exception as e:
        print(f"⚠️ Error fetching weather: {e}")
        return None

# [FIX] Changed input type from 'int' to 'Optional[int]' to satisfy type checkers
def get_weather_emoji(code: Optional[int]) -> str:
    """Maps WMO Weather Codes to Emojis."""
    if code is None: return "❓"
    
    # Open-Meteo uses WMO Weather interpretation codes (WW)
    if code == 0: return "☀️"             # Clear sky
    if code in [1, 2, 3]: return "⛅"    # Partly cloudy
    if code in [45, 48]: return "🌫️"    # Fog
    if code in [51, 53, 55]: return "🌦️" # Drizzle
    if code in [61, 63, 65]: return "🌧️" # Rain
    if code >= 95: return "⛈️"           # Thunderstorm
    return "🌥️"