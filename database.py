from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Configurazione del database
DATABASE_URL = "sqlite:///club_auto_storiche.db"

# Creazione dell'engine
engine = create_engine(DATABASE_URL, echo=True)

# Creazione della sessione
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Inizializza il database creando tutte le tabelle"""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Genera una sessione di database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
