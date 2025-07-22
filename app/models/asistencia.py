from sqlalchemy import Column, Integer, String, ForeignKey, Date, CheckConstraint
from app.db import Base

class Asistencia(Base):
    __tablename__ = "asistencia"

    id_asistencia = Column(Integer, primary_key=True, index=True)
    id_estudiante = Column(Integer, nullable=False)
    id_profesor = Column(Integer, nullable=False)
    id_curso = Column(Integer, nullable=False)
    id_asignatura = Column(Integer, nullable=False)
    fecha = Column(Date, nullable=False)
    presente = Column(Integer, nullable=False)  # Valores: 1 (Presente), 2 (No Asistió), y 3 (Justificado).
    observaciones = Column(String, nullable=True)
    
    __table_args__ = (
        CheckConstraint('presente IN (1, 2, 3)', name='check_presente_valid'),
    )