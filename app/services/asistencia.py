from sqlalchemy.orm import Session
from sqlalchemy.exc import DataError, IntegrityError
from fastapi import HTTPException
from app.models.asistencia import Asistencia
from app.schemas.asistencia import AsistenciaCreate, AsistenciaUpdate
from app.services.validaciones_externas import (
    validar_estudiante,
    validar_profesor,
    validar_curso,
    validar_asignatura
)
import asyncio

async def create_asistencia(db: Session, asistencia: AsistenciaCreate):
    try:
        # Validar datos externos
        await asyncio.gather(
            validar_estudiante(asistencia.id_estudiante),
            validar_profesor(asistencia.id_profesor),
            validar_curso(asistencia.id_curso),
            validar_asignatura(asistencia.id_asignatura)
        )
        
        # Validar que el valor de 'presente' sea válido
        if asistencia.presente not in [1, 2, 3]:
            raise HTTPException(
                status_code=400, 
                detail="El campo 'presente' debe ser: 1 (Presente), 2 (No Asistió), o 3 (Justificado)"
            )
        
        # Crear el registro
        db_asistencia = Asistencia(**asistencia.dict())
        db.add(db_asistencia)
        db.commit()
        db.refresh(db_asistencia)
        return db_asistencia
        
    except DataError as e:
        db.rollback()
        if "Data truncated for column 'presente'" in str(e):
            raise HTTPException(
                status_code=400, 
                detail="Valor inválido para 'presente'. Debe ser: 1 (Presente), 2 (No Asistió), o 3 (Justificado)"
            )
        raise HTTPException(status_code=400, detail=f"Error de datos: {str(e)}")
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error de integridad: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

async def update_asistencia(db: Session, id_asistencia: int, asistencia_update: AsistenciaUpdate):
    try:
        # Verificar que el registro existe
        db_asistencia = db.query(Asistencia).filter(Asistencia.id_asistencia == id_asistencia).first()
        if not db_asistencia:
            raise HTTPException(status_code=404, detail="Asistencia not found")
        
        # Preparar validaciones externas solo para campos que se van a actualizar
        validaciones = []
        
        if asistencia_update.id_estudiante is not None:
            validaciones.append(validar_estudiante(asistencia_update.id_estudiante))
        
        if asistencia_update.id_profesor is not None:
            validaciones.append(validar_profesor(asistencia_update.id_profesor))
        
        if asistencia_update.id_curso is not None:
            validaciones.append(validar_curso(asistencia_update.id_curso))
        
        if asistencia_update.id_asignatura is not None:
            validaciones.append(validar_asignatura(asistencia_update.id_asignatura))
        
        # Ejecutar validaciones externas
        if validaciones:
            await asyncio.gather(*validaciones)
        
        # Validar que el valor de 'presente' sea válido si se está actualizando
        if asistencia_update.presente is not None and asistencia_update.presente not in [1, 2, 3]:
            raise HTTPException(
                status_code=400, 
                detail="El campo 'presente' debe ser: 1 (Presente), 2 (No Asistió), o 3 (Justificado)"
            )
        
        # Actualizar solo los campos que no sean None
        update_data = asistencia_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            if value is not None:
                setattr(db_asistencia, field, value)
        
        db.commit()
        db.refresh(db_asistencia)
        return db_asistencia
        
    except DataError as e:
        db.rollback()
        if "Data truncated for column 'presente'" in str(e):
            raise HTTPException(
                status_code=400, 
                detail="Valor inválido para 'presente'. Debe ser: 1 (Presente), 2 (No Asistió), o 3 (Justificado)"
            )
        raise HTTPException(status_code=400, detail=f"Error de datos: {str(e)}")
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error de integridad: {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

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

def get_asistencia_por_estudiante_y_fecha(db: Session, id_estudiante: int, fecha):
    """
    Obtiene los registros de asistencia de un estudiante específico en una fecha específica.
    Puede devolver múltiples registros si el estudiante tiene asistencia en varias asignaturas el mismo día.
    """
    return db.query(Asistencia).filter(
        Asistencia.id_estudiante == id_estudiante,
        Asistencia.fecha == fecha
    ).all()
