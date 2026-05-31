import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar variables de entorno desde .env (si existe)
load_dotenv()

# Obtener la ruta de la base de datos desde .env o usar valor por defecto
DATABASE_PATH = os.getenv("DATABASE_PATH", "data/servicio_militar.db")

# Crear la carpeta si no existe
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

# URL de SQLite
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Configurar engine (con check_same_thread=False para CustomTkinter)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

def init_db():
    """Crea todas las tablas definidas en los modelos."""
    # No es necesario importar Recluta, solo asegurar que modelos.py se haya cargado
   
    Base.metadata.create_all(bind=engine)

def get_session():
    """Retorna una nueva sesión de base de datos."""
    return SessionLocal()