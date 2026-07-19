from pathlib import Path
from dotenv import load_dotenv
import os

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to the .env file."
    )

# Database
DATABASE_URL = f"sqlite:///{BASE_DIR / 'data' / 'healthpilot.db'}"

# Application
APP_NAME = "HealthPilot AI"
APP_VERSION = "1.0.0"

# LLM
LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "gemini-3.5-flash",
)

# Default timezone
TIMEZONE = "Asia/Kolkata"