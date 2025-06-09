from fastapi import FastAPI
from app.routers import asistencia
from app.db import init_db, test_connection

app = FastAPI(title="Asistencia API")

@app.on_event("startup")
def startup_event():
    init_db()
    test_connection()

# Registrar rutas
app.include_router(asistencia.router, prefix="/asistencia", tags=["Asistencia"])