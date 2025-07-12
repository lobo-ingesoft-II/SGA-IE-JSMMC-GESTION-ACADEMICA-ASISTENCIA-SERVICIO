import httpx
from fastapi import HTTPException

ASIGNATURAS_API_URL = "http://127.0.0.1:8001/asignaturas/"
CURSOS_API_URL = "http://127.0.0.1:8004/cursos/"
ESTUDIANTES_API_URL = "http://127.0.0.1:8005/estudiantes/"
PROFESORES_API_URL = "http://127.0.0.1:8009/profesor/"

async def validar_asignatura(id_asignatura: int):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{ASIGNATURAS_API_URL}{id_asignatura}")
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail="Asignatura no válida")
        
async def validar_curso(id_curso: int):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{CURSOS_API_URL}{id_curso}")
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail="Curso no válido")

async def validar_estudiante(id_estudiante: int):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{ESTUDIANTES_API_URL}{id_estudiante}")
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail="Estudiante no válido")

async def validar_profesor(id_profesor: int):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{PROFESORES_API_URL}{id_profesor}")
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail="Profesor no válido")