from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.schemas.asistencia import AsistenciaCreate, AsistenciaUpdate, AsistenciaResponse
from app.db import SessionLocal
from datetime import date
from app.services.asistencia import (
    create_asistencia,
    get_asistencia,
    update_asistencia,
    list_asistencia,
    list_asistencia_por_estudiante,
    list_asistencia_por_curso,
    list_asistencia_por_fecha,
    get_asistencia_por_estudiante_y_fecha
)
from app.observabilidad.observabilidad import prometheus_metrics, REQUEST_COUNT, REQUEST_LATENCY, ERROR_COUNT
from prometheus_client import CollectorRegistry, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

router = APIRouter()

@router.get("/custom_metrics", tags=["Observabilidad"])
def custom_metrics():
    """
    Expone las métricas personalizadas de Prometheus para el servicio de asistencia.
    """
    registry = CollectorRegistry()
    registry.register(REQUEST_COUNT)
    registry.register(REQUEST_LATENCY)
    registry.register(ERROR_COUNT)
    return Response(generate_latest(registry), media_type=CONTENT_TYPE_LATEST)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AsistenciaResponse, summary="Registrar asistencia", tags=["Asistencia"])
@prometheus_metrics("create_asistencia")
async def create(asistencia: AsistenciaCreate, db: Session = Depends(get_db), request: Request = None):
    """
    Registra una nueva asistencia después de validar los datos externos.
    
    **Valores válidos para 'presente':**
    - 1: Presente
    - 2: No Asistió  
    - 3: Justificado
    
    **Ejemplo de request:**
    ```json
    {
        "id_estudiante": 1,
        "id_profesor": 11,
        "id_curso": 1,
        "id_asignatura": 1,
        "fecha": "2025-07-10",
        "presente": 1,
        "observaciones": "Estudiante participativo"
    }
    ```
    """
    return await create_asistencia(db, asistencia)

@router.put("/{id_asistencia}", response_model=AsistenciaResponse, summary="Actualizar asistencia", tags=["Asistencia"])
@prometheus_metrics("update_asistencia")
async def update(id_asistencia: int, asistencia_update: AsistenciaUpdate, db: Session = Depends(get_db), request: Request = None):
    """
    Actualiza un registro de asistencia existente.
    
    Permite actualizar cualquier campo de la asistencia de forma parcial.
    Solo se actualizarán los campos que se envíen en el request.
    
    **Valores válidos para 'presente':**
    - 1: Presente
    - 2: No Asistió  
    - 3: Justificado
    
    **Ejemplo de request (actualización parcial):**
    ```json
    {
        "presente": 2,
        "observaciones": "Falta justificada por enfermedad"
    }
    ```
    
    **Ejemplo de request (actualización completa):**
    ```json
    {
        "id_estudiante": 1,
        "id_profesor": 11,
        "id_curso": 1,
        "id_asignatura": 1,
        "fecha": "2025-07-11",
        "presente": 3,
        "observaciones": "Justificado por cita médica"
    }
    ```
    """
    return await update_asistencia(db, id_asistencia, asistencia_update)

@router.get("/{id_asistencia}", response_model=AsistenciaResponse, summary="Obtener asistencia por ID", tags=["Asistencia"])
@prometheus_metrics("get_asistencia")
async def get(id_asistencia: int, db: Session = Depends(get_db), request: Request = None):
    """
    Obtiene un registro de asistencia por su ID.
    """
    db_asistencia = get_asistencia(db, id_asistencia)
    if not db_asistencia:
        raise HTTPException(status_code=404, detail="Asistencia not found")
    return db_asistencia

@router.get("/", response_model=list[AsistenciaResponse], summary="Listar todas las asistencias", tags=["Asistencia"])
@prometheus_metrics("list_asistencia")
async def list_all(db: Session = Depends(get_db), request: Request = None):
    """
    Lista todas las asistencias registradas.
    """
    return list_asistencia(db)

@router.get("/por_estudiante/{id_estudiante}", response_model=list[AsistenciaResponse], summary="Listar asistencias por estudiante", tags=["Asistencia"])
@prometheus_metrics("list_asistencia_por_estudiante")
async def list_by_estudiante(id_estudiante: int, db: Session = Depends(get_db), request: Request = None):
    """
    Lista todas las asistencias de un estudiante.
    """
    return list_asistencia_por_estudiante(db, id_estudiante)

@router.get("/por_estudiante/{id_estudiante}/fecha/{fecha}", response_model=list[AsistenciaResponse], summary="Obtener asistencia por estudiante y fecha", tags=["Asistencia"])
@prometheus_metrics("get_asistencia_por_estudiante_y_fecha")
async def get_by_estudiante_and_fecha(id_estudiante: int, fecha: date, db: Session = Depends(get_db), request: Request = None):
    """
    Obtiene los registros de asistencia de un estudiante específico en una fecha específica.
    
    Este endpoint es útil para:
    - Verificar si un estudiante asistió en una fecha específica
    - Obtener todas las asignaturas en las que el estudiante tuvo clases en una fecha
    - Revisar el estado de asistencia de un estudiante en un día particular
    
    **Parámetros:**
    - `id_estudiante`: ID del estudiante
    - `fecha`: Fecha en formato YYYY-MM-DD (ej: 2025-07-11)
    
    **Posibles respuestas:**
    - Lista vacía `[]`: El estudiante no tuvo clases registradas en esa fecha
    - Una o más asistencias: El estudiante tuvo clases en esa fecha
    
    **Ejemplo de URL:**
    ```
    GET /asistencia/por_estudiante/123/fecha/2025-07-11
    ```
    """
    asistencias = get_asistencia_por_estudiante_y_fecha(db, id_estudiante, fecha)
    return asistencias

@router.get("/por_curso/{id_curso}", response_model=list[AsistenciaResponse], summary="Listar asistencias por curso", tags=["Asistencia"])
@prometheus_metrics("list_asistencia_por_curso")
async def list_by_curso(id_curso: int, db: Session = Depends(get_db), request: Request = None):
    """
    Lista todas las asistencias de un curso.
    """
    return list_asistencia_por_curso(db, id_curso)

@router.get("_val/valores-validos", summary="Obtener valores válidos para asistencia", tags=["Asistencia"])
@prometheus_metrics("get_valores_validos")
async def get_valores_validos(request: Request = None):
    """
    Obtiene la información sobre los valores válidos para el campo 'presente'.
    """
    return {
        "presente": {
            "1": "Presente",
            "2": "No Asistió", 
            "3": "Justificado"
        },
        "descripcion": "El campo 'presente' debe ser un número entero: 1 (Presente), 2 (No Asistió), o 3 (Justificado)"
    }

@router.get("/por_fecha/{fecha}", response_model=list[AsistenciaResponse], summary="Listar asistencias por fecha", tags=["Asistencia"])
@prometheus_metrics("list_asistencia_por_fecha")
async def list_by_fecha(fecha: date, db: Session = Depends(get_db), request: Request = None):
    """
    Lista todas las asistencias de una fecha específica.
    """
    return list_asistencia_por_fecha(db, fecha)