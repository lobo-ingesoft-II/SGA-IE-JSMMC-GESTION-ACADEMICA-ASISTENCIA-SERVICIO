"""from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "asistencia_http_requests_total",
    "Total de peticiones HTTP en asistencia",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "asistencia_http_request_duration_seconds",
    "Duración de las peticiones HTTP en asistencia",
    ["method", "endpoint"],
    buckets=[0.1, 0.3, 1.0, 2.5, 5.0, 10.0]
)

ERROR_COUNT = Counter(
    "asistencia_http_request_errors_total",
    "Total de errores HTTP (status >= 400) en asistencia",
    ["endpoint", "method", "status_code"]
)

def prometheus_metrics(endpoint_name):
    import time
    from fastapi import Request, HTTPException
    def decorator(func):
        async def wrapper(*args, **kwargs):
            request: Request = kwargs.get("request")
            method = request.method if request else "N/A"
            start_time = time.time()
            try:
                REQUEST_COUNT.labels(method=method, endpoint=endpoint_name).inc()
                response = await func(*args, **kwargs)
                REQUEST_LATENCY.labels(method=method, endpoint=endpoint_name).observe(time.time() - start_time)
                return response
            except HTTPException as e:
                ERROR_COUNT.labels(endpoint=endpoint_name, method=method, status_code=e.status_code).inc()
                REQUEST_LATENCY.labels(method=method, endpoint=endpoint_name).observe(time.time() - start_time)
                raise
        return wrapper
    return decorator"""

from prometheus_client import Counter, Histogram
from fastapi import Request, HTTPException
from functools import wraps
import time

REQUEST_COUNT = Counter(
    "asistencia_http_requests_total",
    "Total de peticiones HTTP en asistencia",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "asistencia_http_request_duration_seconds",
    "Duración de las peticiones HTTP en asistencia",
    ["method", "endpoint"],
    buckets=[0.1, 0.3, 1.0, 2.5, 5.0, 10.0]
)

ERROR_COUNT = Counter(
    "asistencia_http_request_errors_total",
    "Total de errores HTTP (status >= 400) en asistencia",
    ["endpoint", "method", "status_code"]
)

def prometheus_metrics(endpoint_name):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Buscar instancia de Request en *args
            request = next((arg for arg in args if isinstance(arg, Request)), None)
            method = request.method if request else "N/A"
            start_time = time.time()
            try:
                REQUEST_COUNT.labels(method=method, endpoint=endpoint_name).inc()
                response = await func(*args, **kwargs)
                REQUEST_LATENCY.labels(method=method, endpoint=endpoint_name).observe(time.time() - start_time)
                return response
            except HTTPException as e:
                ERROR_COUNT.labels(endpoint=endpoint_name, method=method, status_code=e.status_code).inc()
                REQUEST_LATENCY.labels(method=method, endpoint=endpoint_name).observe(time.time() - start_time)
                raise
        return wrapper
    return decorator
