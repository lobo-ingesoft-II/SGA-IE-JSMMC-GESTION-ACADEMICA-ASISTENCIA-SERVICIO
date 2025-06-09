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
