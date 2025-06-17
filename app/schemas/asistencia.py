from pydantic import BaseModel
from datetime import date

class AsistenciaBase(BaseModel):
    id_estudiante: int
    id_profesor: int
    id_curso: int
    id_asignatura: int
    fecha: date
    presente: int
    observaciones: str | None

class AsistenciaCreate(AsistenciaBase):
    pass

class AsistenciaResponse(AsistenciaBase):
    id_asistencia: int

    class Config:
        orm_mode = True