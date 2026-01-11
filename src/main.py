import sys
import random 
from datetime import datetime
from src.config import Config
from src.fetchers.weather import fetch_weather
from src.fetchers.finance import fetch_all_finance
from src.renderer import render_email
from src.mailer import send_email

def main():
    print("🚀 Starting Daily Briefing Bot...")
    
    print("🌤️ Fetching Weather...")
    weather = fetch_weather()
    
    print("📊 Fetching Finance Data...")
    indices, forex = fetch_all_finance()
    
    print("🎨 Rendering Email Template...")
    if not weather:
        weather = {"current_temp": "N/A", "max_temp": "N/A", "min_temp": "N/A", "weather_code": None}

    html_content = render_email(weather, indices, forex)
    
    # [UPDATED] Fun Title Logic
    # Format: "🐨 11 Jan 2026 Daily Briefing"
    
    # Random selection of fun emojis
    emojis = ["🐨", "🚀", "☕", "🗞️", "✨", "🐍", "🌏", "🦄", "📈"]
    selected_emoji = random.choice(emojis)
    
    date_str = datetime.now(Config.TIMEZONE).strftime('%d %b %Y')
    
    subject = f"{selected_emoji} {date_str} Daily Briefing"
    
    success = send_email(html_content, subject=subject)
    
    if not success:
        sys.exit(1)
        
    print("🏁 Task Completed Successfully.")

if __name__ == "__main__":
    main()