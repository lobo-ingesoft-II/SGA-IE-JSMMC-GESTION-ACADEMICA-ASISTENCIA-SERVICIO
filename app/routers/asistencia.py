from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.asistencia import AsistenciaCreate, AsistenciaResponse
from app.services.asistencia import create_asistencia, get_asistencia, list_asistencia
from app.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AsistenciaResponse)
def create(asistencia: AsistenciaCreate, db: Session = Depends(get_db)):
    return create_asistencia(db, asistencia)

@router.get("/{id_asistencia}", response_model=AsistenciaResponse)
def get(id_asistencia: int, db: Session = Depends(get_db)):
    db_asistencia = get_asistencia(db, id_asistencia)
    if not db_asistencia:
        raise HTTPException(status_code=404, detail="Attendance not found")
    return db_asistencia

@router.get("/", response_model=list[AsistenciaResponse])
def list_all(db: Session = Depends(get_db)):
    return list_asistencia(db)