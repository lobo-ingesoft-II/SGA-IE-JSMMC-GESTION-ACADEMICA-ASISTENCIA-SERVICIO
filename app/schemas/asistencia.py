from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional

class AsistenciaBase(BaseModel):
    id_estudiante: int
    id_profesor: int
    id_curso: int
    id_asignatura: int
    fecha: date
    presente: int
    observaciones: Optional[str] = None

    @field_validator('presente')
    @classmethod
    def validar_presente(cls, v):
        if v not in [1, 2, 3]:
            raise ValueError('El campo presente debe ser: 1 (Presente), 2 (No Asistió), o 3 (Justificado)')
        return v

class AsistenciaCreate(AsistenciaBase):
    pass

class AsistenciaUpdate(BaseModel):
    id_estudiante: Optional[int] = None
    id_profesor: Optional[int] = None
    id_curso: Optional[int] = None
    id_asignatura: Optional[int] = None
    fecha: Optional[date] = None
    presente: Optional[int] = None
    observaciones: Optional[str] = None

    @field_validator('presente')
    @classmethod
    def validar_presente(cls, v):
        if v is not None and v not in [1, 2, 3]:
            raise ValueError('El campo presente debe ser: 1 (Presente), 2 (No Asistió), o 3 (Justificado)')
        return v

class AsistenciaResponse(AsistenciaBase):
    id_asistencia: int

    model_config = {"from_attributes": True}