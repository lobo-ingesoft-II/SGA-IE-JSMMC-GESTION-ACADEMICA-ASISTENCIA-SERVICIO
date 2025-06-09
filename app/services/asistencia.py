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