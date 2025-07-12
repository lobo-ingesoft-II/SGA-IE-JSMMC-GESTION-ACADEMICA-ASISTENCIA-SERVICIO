from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routers import asistencia
from app.db import init_db, test_connection

# Configurar el ciclo de vida de la aplicación
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    # test_connection()
    yield
    # Shutdown (si necesitas limpiar recursos)

app = FastAPI(title="Asistencia API", lifespan=lifespan)

# Configura los orígenes permitidos para CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",  # Puerto alternativo común para desarrollo
    "http://127.0.0.1:3001",
    "http://localhost:8080",  # Puerto alternativo común
    "http://127.0.0.1:8080",
    # Agrega aquí los dominios de tu frontend en producción
]

# Configurar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Registrar rutas
app.include_router(asistencia.router, prefix="/asistencia", tags=["Asistencia"])