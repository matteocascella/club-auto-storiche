from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Socio(Base):
    """Modello per i soci del club"""
    __tablename__ = 'soci'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cognome = Column(String(50), nullable=False)
    data_nascita = Column(Date)
    email = Column(String(100), unique=True)
    telefono = Column(String(20))
    
    # Relazione con le auto
    auto = relationship("Auto", back_populates="proprietario")

class Auto(Base):
    """Modello per le auto storiche"""
    __tablename__ = 'auto'

    id = Column(Integer, primary_key=True)
    marca = Column(String(50), nullable=False)
    modello = Column(String(50), nullable=False)
    anno = Column(Integer, nullable=False)
    targa = Column(String(20), unique=True)
    proprietario_id = Column(Integer, ForeignKey('soci.id'))
    
    # Relazione con il socio
    proprietario = relationship("Socio", back_populates="auto")

class Evento(Base):
    """Modello per gli eventi del club"""
    __tablename__ = 'eventi'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    data = Column(Date, nullable=False)
    luogo = Column(String(200))
    descrizione = Column(String(500))
    quota_iscrizione = Column(Float)

class Tesseramento(Base):
    """Modello per i tesseramenti annuali"""
    __tablename__ = 'tesseramenti'

    id = Column(Integer, primary_key=True)
    socio_id = Column(Integer, ForeignKey('soci.id'))
    anno = Column(Integer, nullable=False)
    data_pagamento = Column(Date)
    importo = Column(Float, nullable=False)
    
    # Relazione con il socio
    socio = relationship("Socio")
