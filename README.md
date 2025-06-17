# Servicio de Asistencia

## Descripción

Este servicio permite gestionar la asistencia de los estudiantes en el sistema académico. Proporciona funcionalidades para registrar, obtener y listar asistencias, así como consultar la asistencia por curso, estudiante o fecha. Facilita la integración con otros módulos del sistema académico.

- **presente:**  
  - `"1"` = Presente  
  - `"2"` = No Asistió  
  - `"3"` = Justificado

## Endpoints

### Registrar asistencia

**POST** `/asistencias/`

#### Request Body

```json
{
    "id_estudiante": 1,
    "id_profesor": 5,
    "id_curso": 2,
    "id_asignatura": 3,
    "fecha": "2024-06-10",
    "presente": "1",
    "observaciones": "Llegó tarde"
}
```

#### Response

**Status:** 200 OK

```json
{
    "id_asistencia": 1,
    "id_estudiante": 1,
    "id_profesor": 5,
    "id_curso": 2,
    "id_asignatura": 3,
    "fecha": "2024-06-10",
    "presente": "1",
    "observaciones": "Llegó tarde"
}
```

### Obtener asistencia por ID

**GET** `/asistencias/{id_asistencia}`

#### Response

**Status:** 200 OK

```json
{
    "id_asistencia": 1,
    "id_estudiante": 1,
    "id_profesor": 5,
    "id_curso": 2,
    "id_asignatura": 3,
    "fecha": "2024-06-10",
    "presente": "1",
    "observaciones": "Llegó tarde"
}
```

**Status:** 404 Not Found

```json
{
    "detail": "Asistencia not found"
}
```

### Listar todas las asistencias

**GET** `/asistencias/`

#### Response

**Status:** 200 OK

```json
[
    {
        "id_asistencia": 1,
        "id_estudiante": 1,
        "id_profesor": 5,
        "id_curso": 2,
        "id_asignatura": 3,
        "fecha": "2024-06-10",
        "presente": "1",
        "observaciones": "Llegó tarde"
    }
]

### 🔍 Consultar Asistencias por Estudiante

**Endpoint:** `GET /asistencia/estudiante/{id_estudiante}`

Devuelve un listado de todas las asistencias registradas para un estudiante específico identificado por su ID.

#### Parámetros de ruta:
- `id_estudiante` (int): ID único del estudiante.

#### Respuesta exitosa (`200 OK`):
```json
[
  {
    "id": 1,
    "fecha": "2025-06-17",
    "id_estudiante": 42,
    "estado": "Presente"
  },
  {
    "id": 2,
    "fecha": "2025-06-18",
    "id_estudiante": 42,
    "estado": "Ausente"
  }
]

### Respuesta si el estudiante no tiene registros (`404 Not Found`):
```json
{
  "detail": "No se encontraron registros de asistencia para el estudiante con ID 42"
}

## Instalación

1. Asegúrate de tener el entorno configurado:

    ```bash
    pip install -r requirements.txt
    ```
2. Configura la base de datos en el archivo `.env`:

    ```env
    DATABASE_URL="mysql+pymysql://user:password@host:port/database"
    ```
3. Ejecuta el servidor:

    ```bash
    uvicorn app.main:app --reload --port 8002
    ```

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest app/tests/test_asistencia.py
```

## Dependencias

* **FastAPI**: Framework principal.
* **SQLAlchemy**: ORM para manejar la base de datos.
* **Pytest**: Framework para pruebas unitarias.

## Contacto

Para más información, contactar con el equipo de desarrollo.

## Documentación interactiva

Accede a la documentación Swagger en [http://localhost:8002/docs](http://localhost:8002/docs) o ReDoc en [http://localhost:8002/redoc](http://localhost:8002/redoc).