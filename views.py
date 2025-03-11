from sqlalchemy.orm import Session
from models import Socio, Auto, Evento, Tesseramento
from datetime import date

class GestioneSoci:
    @staticmethod
    def aggiungi_socio(db: Session, nome: str, cognome: str, data_nascita: date, 
                       email: str, telefono: str):
        """Aggiunge un nuovo socio al database"""
        nuovo_socio = Socio(
            nome=nome, 
            cognome=cognome, 
            data_nascita=data_nascita,
            email=email, 
            telefono=telefono
        )
        db.add(nuovo_socio)
        db.commit()
        db.refresh(nuovo_socio)
        return nuovo_socio

    @staticmethod
    def lista_soci(db: Session):
        """Restituisce la lista di tutti i soci"""
        return db.query(Socio).all()

    @staticmethod
    def modifica_socio(db: Session, socio_id: int, **kwargs):
        """Modifica i dati di un socio"""
        socio = db.query(Socio).filter(Socio.id == socio_id).first()
        if socio:
            for key, value in kwargs.items():
                setattr(socio, key, value)
            db.commit()
            db.refresh(socio)
        return socio

class GestioneAuto:
    @staticmethod
    def aggiungi_auto(db: Session, marca: str, modello: str, anno: int, 
                      targa: str, proprietario_id: int):
        """Aggiunge una nuova auto al database"""
        nuova_auto = Auto(
            marca=marca, 
            modello=modello, 
            anno=anno,
            targa=targa, 
            proprietario_id=proprietario_id
        )
        db.add(nuova_auto)
        db.commit()
        db.refresh(nuova_auto)
        return nuova_auto

    @staticmethod
    def lista_auto(db: Session):
        """Restituisce la lista di tutte le auto"""
        return db.query(Auto).all()

class GestioneEventi:
    @staticmethod
    def crea_evento(db: Session, nome: str, data: date, luogo: str, 
                    descrizione: str, quota_iscrizione: float):
        """Crea un nuovo evento"""
        nuovo_evento = Evento(
            nome=nome,
            data=data,
            luogo=luogo,
            descrizione=descrizione,
            quota_iscrizione=quota_iscrizione
        )
        db.add(nuovo_evento)
        db.commit()
        db.refresh(nuovo_evento)
        return nuovo_evento

    @staticmethod
    def lista_eventi(db: Session):
        """Restituisce la lista di tutti gli eventi"""
        return db.query(Evento).all()

class GestioneTesseramenti:
    @staticmethod
    def registra_tesseramento(db: Session, socio_id: int, anno: int, 
                               data_pagamento: date, importo: float):
        """Registra un nuovo tesseramento per un socio"""
        nuovo_tesseramento = Tesseramento(
            socio_id=socio_id,
            anno=anno,
            data_pagamento=data_pagamento,
            importo=importo
        )
        db.add(nuovo_tesseramento)
        db.commit()
        db.refresh(nuovo_tesseramento)
        return nuovo_tesseramento

    @staticmethod
    def verifica_tesseramento(db: Session, socio_id: int, anno: int):
        """Verifica se un socio ha un tesseramento valido per un determinato anno"""
        return db.query(Tesseramento).filter(
            Tesseramento.socio_id == socio_id,
            Tesseramento.anno == anno
        ).first() is not None
