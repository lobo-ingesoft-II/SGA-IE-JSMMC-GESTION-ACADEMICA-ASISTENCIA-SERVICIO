from sqlalchemy.orm import Session
from app.models.asistencia import Asistencia
from app.schemas.asistencia import AsistenciaCreate

def create_asistencia(db: Session, asistencia: AsistenciaCreate):
    db_asistencia = Asistencia(**asistencia.dict())
    db.add(db_asistencia)
    db.commit()
    db.refresh(db_asistencia)
    return db_asistencia

def get_asistencia(db: Session, id_asistencia: int):
    return db.query(Asistencia).filter(Asistencia.id_asistencia == id_asistencia).first()

def list_asistencia(db: Session):
    return db.query(Asistencia).all()

def list_asistencia_by_estudiante(db: Session, id_estudiante: int):
    """
    Devuelve todas las entradas de asistencia para un estudiante dado.
    """
    return (
        db
        .query(Asistencia)
        .filter(Asistencia.id_estudiante == id_estudiante)
        .all()
    )