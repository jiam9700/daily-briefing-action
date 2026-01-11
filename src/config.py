import os
import sys
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

load_dotenv()

class Config:
    # --- Basic Settings ---
    TIMEZONE = ZoneInfo("Australia/Melbourne")
    
    # --- Location (User's Home) ---
    # [UPDATED] Now loaded from Environment Variables for privacy
    # Defaulting to Melbourne CBD only if variables are missing
    try:
        LATITUDE = float(os.getenv("LATITUDE", "-37.8136"))
        LONGITUDE = float(os.getenv("LONGITUDE", "144.9631"))
    except ValueError:
        # Fallback if the string cannot be converted to float
        print("⚠️ Invalid coordinates in environment variables. Using default.")
        LATITUDE = -37.8136
        LONGITUDE = 144.9631

    LOCATION_NAME = os.getenv("LOCATION_NAME", "Melbourne CBD")
    
    # --- Email Service Configuration (SMTP) ---
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com") 
    SMTP_PORT = int(os.getenv("SMTP_PORT", 465))             
    SMTP_USER = os.getenv("SMTP_USER", "")                       
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")               
    
    # --- Sender & Receiver ---
    SENDER_EMAIL = SMTP_USER
    RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "")

    # --- Watchlist ---
    INDICES = ["QQQ", "DIA", "SPY", "^VIX"]
    FOREX_PAIRS = ["AUDCNY=X", "AUDUSD=X"]

    @classmethod
    def validate(cls):
        required_vars = ["SMTP_USER", "SMTP_PASSWORD", "RECEIVER_EMAIL"]
        missing = [key for key in required_vars if not getattr(cls, key)]
        if missing:
            print(f"❌ Critical Error: Missing environment variables: {', '.join(missing)}")
            sys.exit(1)

Config.validate()