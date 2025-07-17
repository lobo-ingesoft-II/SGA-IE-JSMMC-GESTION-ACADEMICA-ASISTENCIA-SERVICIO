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

## [1.0.3] - 2025-07-05
### Agregado
- Endpoints para listar asistencias por estudiante, curso y fecha.
- Validaciones externas para estudiante, profesor, curso y asignatura.
- Mejor documentación Swagger en los endpoints.

### Cambiado
- Se mejoró la modularidad y separación de responsabilidades siguiendo SOFEA.
- Se actualizó requirements.txt para incluir httpx.

## [1.0.4] - 2025-07-07
### Corregido
- Se hacen ajustes/correcciones en archivos routers/asistencia.py, services/asistencia.py y validaciones_externas.py

## [1.0.5] - 2025-07-13
### Agregado
- Implementación del middleware de observabilidad con Prometheus en `observabilidad/observabilidad.py`.
- Decorador `@prometheus_metrics` aplicado a **todos los endpoints** del router de asistencia para recolectar métricas HTTP (conteo y duración).
- Métricas exportadas en el endpoint `/metrics`.
- Nuevas pruebas unitarias agregadas en `app/tests/test_asistencia.py`, cubriendo casos de éxito y error para creación, consulta individual, consulta múltiple, y endpoints adicionales.
- Endpoint `/asistencia/valores-validos` documentado y probado, que devuelve los valores permitidos para el campo `presente`.
- Se agregó documentación Swagger detallada en todos los endpoints, con ejemplos y respuestas esperadas.
- Se refactorizó la validación externa para estudiante, profesor, curso y asignatura como funciones asíncronas.

### Cambiado
- Todos los endpoints ahora utilizan funciones `async def` para soportar mejor concurrencia y observabilidad.
- El router `asistencia.py` fue modularizado según principios SOFEA, separando responsabilidades y mejorando la legibilidad del código.
- Documentación enriquecida con descripciones y ejemplos para facilitar el uso de la API desde Swagger/OpenAPI.