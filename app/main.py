from fastapi import FastAPI
from app.routers import asistencia
from app.db import init_db

app = FastAPI(title="Attendance API")

@app.on_event("startup")
def startup_event():
    init_db()

# Registrar rutas
app.include_router(asistencia.router, prefix="/asistencia", tags=["Asistencia"])