# Changelog - Servicio de Asistencia

## [1.0.0] - 2025-06-09
### Agregado
- Creación del servicio de asistencia.
- Endpoint **POST** `/asistencia/` para registrar un nuevo registro de asistencia.
- Endpoint **GET** `/asistencia/{id_asistencia}` para obtener un registro de asistencia por ID.
- Endpoint **GET** `/asistencia/` para listar todos los registros de asistencia.
- Integración de modelos, esquemas y servicios con SQLAlchemy y Pydantic.
- Pruebas unitarias básicas para las operaciones CRUD de asistencia.

## [1.0.1] - 2025-06-09
### Corregido
- Validación adicional para la fecha en el registro de asistencia.
- Mejora en los mensajes de error para registros no encontrados.

## [1.0.2] - 2025-06-10
### Corregido
- Correción del puerto en README.md a 8002.
### Cambiado
- Se añadieron claves foráneas (FKs) en el modelo de asistencia.
- El atributo `presente` ahora solo acepta los valores 1 (Presente), 2 (No Asistió), y 3 (Justificado).
- Se ajusta readme.
### Agregado
- Adición de sección documentación interactiva.
<<<<<<< Updated upstream
## [1.1.0] - 2025-06-17
### Agregado
- Nuevo endpoint `GET /asistencia/estudiante/{id_estudiante}` para consultar todas las asistencias registradas de un estudiante específico.
- Documentación del funcionamiento del endpoint en el README
=======

## [1.1.0] - 2025-07-05
### Agregado
- Endpoints para listar asistencias por estudiante, curso y fecha.
- Validaciones externas para estudiante, profesor, curso y asignatura.
- Mejor documentación Swagger en los endpoints.

### Cambiado
- Se mejoró la modularidad y separación de responsabilidades siguiendo SOFEA.
- Se actualizó requirements.txt para incluir httpx.
>>>>>>> Stashed changes
