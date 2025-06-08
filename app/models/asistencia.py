from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.db import Base

class Asistencia(Base):
    __tablename__ = "asistencia"

    id_asistencia = Column(Integer, primary_key=True, index=True)
    id_estudiante = Column(Integer, ForeignKey("estudiantes.id_estudiante"), nullable=False)
    id_profesor = Column(Integer, ForeignKey("profesores.id_profesor"), nullable=False)
    id_curso = Column(Integer, ForeignKey("cursos.id_curso"), nullable=False)
    id_asignatura = Column(Integer, ForeignKey("asignaturas.id_asignatura"), nullable=False)
    fecha = Column(Date, nullable=False)
    presente = Column(String(1), nullable=False)  # Valores: "A", "F", "J"
    observaciones = Column(String, nullable=True)