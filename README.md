# Servicio de Asistencia

## Descripción

Este servicio permite gestionar la asistencia de los estudiantes en el sistema académico. Proporciona funcionalidades para registrar, obtener y listar asistencias, así como consultar la asistencia por curso, estudiante o fecha. Facilita la integración con otros módulos del sistema académico.

## Endpoints

### Registrar asistencia

**POST** `/asistencias/`

#### Request Body

```json
{
    "id_estudiante": 1,
    "id_curso": 2,
    "fecha": "2024-06-10",
    "presente": true
}
```

#### Response

**Status:** 200 OK

```json
{
    "id_asistencia": 1,
    "id_estudiante": 1,
    "id_curso": 2,
    "fecha": "2024-06-10",
    "presente": true
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
    "id_curso": 2,
    "fecha": "2024-06-10",
    "presente": true
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
        "id_curso": 2,
        "fecha": "2024-06-10",
        "presente": true
    },
    {
        "id_asistencia": 2,
        "id_estudiante": 2,
        "id_curso": 2,
        "fecha": "2024-06-10",
        "presente": false
    }
]
```

### Consultar asistencias por estudiante

**GET** `/asistencias/estudiante/{id_estudiante}`

#### Response

**Status:** 200 OK

```json
[
    {
        "id_asistencia": 1,
        "id_estudiante": 1,
        "id_curso": 2,
        "fecha": "2024-06-10",
        "presente": true
    }
]
```

### Consultar asistencias por curso

**GET** `/asistencias/curso/{id_curso}`

#### Response

**Status:** 200 OK

```json
[
    {
        "id_asistencia": 1,
        "id_estudiante": 1,
        "id_curso": 2,
        "fecha": "2024-06-10",
        "presente": true
    }
]
```

### Consultar asistencias por fecha

**GET** `/asistencias/fecha/{fecha}`

#### Response

**Status:** 200 OK

```json
[
    {
        "id_asistencia": 1,
        "id_estudiante": 1,
        "id_curso": 2,
        "fecha": "2024-06-10",
        "presente": true
    }
]
```

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
    uvicorn app.main:app --reload
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
