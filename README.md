# Servicio de Asistencia

## Descripción

Este servicio permite gestionar la asistencia de los estudiantes en el sistema académico. Proporciona funcionalidades para registrar, obtener y listar asistencias, así como consultar la asistencia por curso, estudiante o fecha. Integra validaciones externas para asegurar la integridad de los datos.

- **presente:**  
  - `"1"` = Presente  
  - `"2"` = No Asistió  
  - `"3"` = Justificado

## Endpoints

### Registrar asistencia

**POST** `/asistencia/`

Valida que el estudiante, profesor, curso y asignatura existan en sus respectivos servicios antes de registrar la asistencia.

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

**GET** `/asistencia/{id_asistencia}`

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

**GET** `/asistencia/`

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
```

### Listar asistencias por estudiante

**GET** `/asistencia/por_estudiante/{id_estudiante}`

### Listar asistencias por curso

**GET** `/asistencia/por_curso/{id_curso}`

### Listar asistencias por fecha

**GET** `/asistencia/por_fecha/{fecha}`

## Validaciones externas

- **id_estudiante**: Valida contra el API de Estudiantes.
- **id_profesor**: Valida contra el API de Autenticación.
- **id_curso**: Valida contra el API de Cursos.
- **id_asignatura**: Valida contra el API de Asignaturas.

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
```
## Endpoints

...

### Obtener valores válidos para el campo `presente`

**GET** `/asistencia/valores-validos`

Devuelve los valores aceptados por el campo `presente`:

#### Response

**Status:** 200 OK

```json
{
    "valores_validos": {
        "1": "Presente",
        "2": "No Asistió",
        "3": "Justificado"
    }
}
```

## Instalación

1. Instala dependencias:
    ```bash
    pip install -r requirements.txt
    ```
2. Configura la base de datos en el archivo `.env`:
    ```env
    DATABASE_URL="mysql+pymysql://user:password@host:port/asistencia_db"
    ```
3. Ejecuta el servidor:
    ```bash
    uvicorn app.main:app --reload --port 8002
    ```

## Documentación interactiva

Accede a la documentación Swagger en [http://localhost:8002/docs](http://localhost:8002/docs) o ReDoc en [http://localhost:8002/redoc](http://localhost:8002/redoc).

## Observabilidad y métricas

El servicio expone métricas Prometheus para todos los endpoints, permitiendo monitoreo de:
- Total de peticiones HTTP por endpoint y método
- Latencia de cada petición
- Total de errores HTTP (status >= 400)

**Endpoint de métricas Prometheus:**
```
GET /asistencia/custom_metrics
```

Puedes consultar estas métricas desde Prometheus o navegando directamente al endpoint.

## Pruebas unitarias

Las pruebas unitarias se encuentran en `app/tests/test_asistencia.py` y cubren:
- Casos exitosos y de error para todos los endpoints principales
- Validaciones de datos y respuestas esperadas

Para ejecutar los tests:
```bash
pytest app/tests/
```
