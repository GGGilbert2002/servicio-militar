import os
from dotenv import load_dotenv

load_dotenv()

# Variables de entorno con valores por defecto
APP_NAME = os.getenv("APP_NAME", "Sistema de Reclutamiento - Coro")
WINDOW_SIZE = os.getenv("WINDOW_SIZE", "1024x768")

# Parroquias: si viene del .env se usa, sino la lista por defecto
_parroquias_env = os.getenv("PARROQUIAS_CORO")
if _parroquias_env:
    PARROQUIAS = [p.strip() for p in _parroquias_env.split(",")]
else:
    PARROQUIAS = ["San Antonio", "San Gabriel", "Santa Ana", "San Nicolás", "San Clemente", "San José"]

DEBUG = os.getenv("DEBUG", "False").lower() == "true"