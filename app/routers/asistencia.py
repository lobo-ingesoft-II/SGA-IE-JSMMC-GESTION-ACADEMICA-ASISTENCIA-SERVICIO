from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.asistencia import AsistenciaCreate, AsistenciaResponse
from app.services.asistencia import create_asistencia, get_asistencia, list_asistencia, list_asistencia_by_estudiante
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

@router.get(
    "/estudiante/{id_estudiante}",
    response_model=list[AsistenciaResponse],
    summary="Listar todas las asistencias de un estudiante por su ID",
)
def read_asistencias_por_estudiante(
    id_estudiante: int,
    db: Session = Depends(get_db),
):
    """
    Devuelve todas las asistencias del estudiante cuyo ID se pasa en la ruta.
    Lanza un error 404 si el estudiante no tiene registros de asistencia.
    """
    asistencias = list_asistencia_by_estudiante(db, id_estudiante)
    if not asistencias:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontraron registros de asistencia para el estudiante con ID {id_estudiante}"
        )
    return asistencias