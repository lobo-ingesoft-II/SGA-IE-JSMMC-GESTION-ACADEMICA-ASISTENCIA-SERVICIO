from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routers import asistencia
from app.db import init_db, test_connection

from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
from starlette.responses import Response
from app.routers.asistencia import REQUEST_COUNT_ASISTENCIA_ROUTERS, REQUEST_LATENCY_ASISTENCIA_ROUTERS, ERROR_COUNT_ASISTENCIA_ROUTERS

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

# Configurar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    try:
        response = await call_next(request)
        status = response.status_code
    except Exception as e:
        status = 500
        raise e
    finally:
        latency = time.time() - start_time
        endpoint = request.url.path
        method = request.method

        REQUEST_COUNT_ASISTENCIA_ROUTERS.labels(endpoint=endpoint, method=method).inc()
        REQUEST_LATENCY_ASISTENCIA_ROUTERS.labels(endpoint=endpoint, method=method).observe(latency)


        
        if status >= 400: # type: ignore
            ERROR_COUNT_ASISTENCIA_ROUTERS.labels(endpoint=endpoint, method=method, status_code=str(status)).inc() # type: ignore

    return response


# Registrar rutas
app.include_router(asistencia.router, prefix="/asistencia", tags=["Asistencia"])