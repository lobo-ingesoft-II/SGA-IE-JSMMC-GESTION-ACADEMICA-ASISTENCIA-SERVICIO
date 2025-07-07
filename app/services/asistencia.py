from sqlalchemy.orm import Session
from app.models.asistencia import Asistencia
from app.schemas.asistencia import AsistenciaCreate
from app.services.validaciones_externas import (
    validar_estudiante,
    validar_profesor,
    validar_curso,
    validar_asignatura
)
import asyncio

async def create_asistencia(db: Session, asistencia: AsistenciaCreate):
    await asyncio.gather(
        validar_estudiante(asistencia.id_estudiante),
        validar_profesor(asistencia.id_profesor),
        validar_curso(asistencia.id_curso),
        validar_asignatura(asistencia.id_asignatura)
    )
    db_asistencia = Asistencia(**asistencia.dict())
    db.add(db_asistencia)
    db.commit()
    db.refresh(db_asistencia)
    return db_asistencia

def get_asistencia(db: Session, id_asistencia: int):
    return db.query(Asistencia).filter(Asistencia.id_asistencia == id_asistencia).first()

def list_asistencia(db: Session):
    return db.query(Asistencia).all()

def list_asistencia_por_estudiante(db: Session, id_estudiante: int):
    return db.query(Asistencia).filter(Asistencia.id_estudiante == id_estudiante).all()

def list_asistencia_por_curso(db: Session, id_curso: int):
    return db.query(Asistencia).filter(Asistencia.id_curso == id_curso).all()

def list_asistencia_por_fecha(db: Session, fecha):
    return db.query(Asistencia).filter(Asistencia.fecha == fecha).all()
