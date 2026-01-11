import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from src.config import Config
from src.fetchers.weather import get_weather_emoji

def render_email(weather_data: dict, indices_data: list, forex_data: list) -> str:
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('email_daily.html')
    
    now = datetime.now(Config.TIMEZONE)
    date_str = now.strftime("%A, %d %B %Y")
    
    w_code = weather_data.get('weather_code') if weather_data else None
    w_emoji = get_weather_emoji(w_code)

    return template.render(
        date_str=date_str,
        location_name=Config.LOCATION_NAME, # [NEW] Pass location name
        weather=weather_data,
        weather_emoji=w_emoji,
        indices=indices_data,
        forex=forex_data
    )