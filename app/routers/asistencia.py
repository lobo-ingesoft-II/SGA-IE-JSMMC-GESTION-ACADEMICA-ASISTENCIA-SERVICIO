from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.asistencia import AsistenciaCreate, AsistenciaResponse
<<<<<<< Updated upstream
from app.services.asistencia import create_asistencia, get_asistencia, list_asistencia, list_asistencia_by_estudiante
=======
from app.services.asistencia import (
    create_asistencia, get_asistencia, list_asistencia,
    list_asistencia_por_estudiante, list_asistencia_por_curso, list_asistencia_por_fecha
)
>>>>>>> Stashed changes
from app.db import SessionLocal
from datetime import date

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AsistenciaResponse, summary="Registrar asistencia", tags=["Asistencia"])
async def create(asistencia: AsistenciaCreate, db: Session = Depends(get_db)):
    """
    Registra una nueva asistencia después de validar los datos externos.
    """
    return await create_asistencia(db, asistencia)

@router.get("/{id_asistencia}", response_model=AsistenciaResponse, summary="Obtener asistencia por ID", tags=["Asistencia"])
def get(id_asistencia: int, db: Session = Depends(get_db)):
    """
    Obtiene un registro de asistencia por su ID.
    """
    db_asistencia = get_asistencia(db, id_asistencia)
    if not db_asistencia:
        raise HTTPException(status_code=404, detail="Asistencia not found")
    return db_asistencia

@router.get("/", response_model=list[AsistenciaResponse], summary="Listar todas las asistencias", tags=["Asistencia"])
def list_all(db: Session = Depends(get_db)):
<<<<<<< Updated upstream
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
=======
    """
    Lista todas las asistencias registradas.
    """
    return list_asistencia(db)

@router.get("/por_estudiante/{id_estudiante}", response_model=list[AsistenciaResponse], summary="Listar asistencias por estudiante", tags=["Asistencia"])
def list_by_estudiante(id_estudiante: int, db: Session = Depends(get_db)):
    """
    Lista todas las asistencias de un estudiante.
    """
    return list_asistencia_por_estudiante(db, id_estudiante)

@router.get("/por_curso/{id_curso}", response_model=list[AsistenciaResponse], summary="Listar asistencias por curso", tags=["Asistencia"])
def list_by_curso(id_curso: int, db: Session = Depends(get_db)):
    """
    Lista todas las asistencias de un curso.
    """
    return list_asistencia_por_curso(db, id_curso)

@router.get("/por_fecha/{fecha}", response_model=list[AsistenciaResponse], summary="Listar asistencias por fecha", tags=["Asistencia"])
def list_by_fecha(fecha: date, db: Session = Depends(get_db)):
    """
    Lista todas las asistencias de una fecha específica.
    """
    return list_asistencia_por_fecha(db, fecha)
>>>>>>> Stashed changes
