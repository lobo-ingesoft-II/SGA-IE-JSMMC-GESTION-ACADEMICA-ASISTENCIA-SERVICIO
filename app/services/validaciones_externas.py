import httpx
from fastapi import HTTPException

async def validar_estudiante(id_estudiante: int):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"http://estudiantes_api/estudiantes/{id_estudiante}")
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail="Estudiante no válido")

async def validar_profesor(id_profesor: int):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"http://autenticacion_api/profesores/{id_profesor}")
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail="Profesor no válido")

async def validar_curso(id_curso: int):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"http://cursos_api/cursos/{id_curso}")
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail="Curso no válido")

async def validar_asignatura(id_asignatura: int):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"http://asignaturas_api/asignaturas/{id_asignatura}")
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail="Asignatura no válida")