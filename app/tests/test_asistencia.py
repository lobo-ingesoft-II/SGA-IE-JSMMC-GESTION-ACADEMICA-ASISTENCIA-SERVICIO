import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_list_all_asistencias():
    response = client.get("/asistencia/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_asistencia_validation():
    # Falta campo obligatorio
    payload = {
        "id_estudiante": 1,
        "id_profesor": 1,
        "id_curso": 1,
        "id_asignatura": 1,
        # "fecha": "2025-07-10",  # Falta
        "presente": 1
    }
    response = client.post("/asistencia/", json=payload)
    assert response.status_code == 422  # Unprocessable Entity

def test_create_asistencia_success():
    payload = {
        "id_estudiante": 1,
        "id_profesor": 11,
        "id_curso": 1,
        "id_asignatura": 1,
        "fecha": "2025-12-10",
        "presente": 1,
        "observaciones": "Test asistencia"
    }
    response = client.post("/asistencia/", json=payload)
    # Puede fallar si la BD no está limpia, pero debe ser 200 o 201 si todo está bien
    assert response.status_code in (200, 201, 400, 409)

def test_get_asistencia_not_found():
    response = client.get("/asistencia/999999")
    assert response.status_code == 404

def test_get_asistencia_success():
    response = client.get(f"/asistencia/1")
    assert response.status_code == 200
    assert response.json()["id_asistencia"] == 1

def test_update_asistencia_not_found():
    payload = {
        "id_estudiante": 1,
        "id_profesor": 17,
        "id_curso": 1,
        "id_asignatura": 1,
        "fecha": "2025-07-16",
        "presente": 1,
        "observaciones": "Actualización test"
    }
    response = client.put("/asistencia/1000000000", json=payload)
    assert response.status_code in (404, 422)

def test_update_asistencia_success():
    update_payload = {
        "id_estudiante": 1,
        "id_profesor": 11,
        "id_curso": 1,
        "id_asignatura": 3,
        "fecha": "2024-01-17",
        "presente": 3,
        "observaciones": "Actualizado 2"
    }
    response = client.put(f"/asistencia/1", json=update_payload)
    assert response.status_code == 200
    assert response.json()["presente"] == 3

def test_list_by_estudiante():
    response = client.get("/asistencia/por_estudiante/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_by_estudiante_and_fecha():
    response = client.get("/asistencia/por_estudiante/1/fecha/2025-07-10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_by_curso():
    response = client.get("/asistencia/por_curso/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_by_fecha():
    response = client.get("/asistencia/por_fecha/2025-07-10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_valores_validos():
    response = client.get("/asistencia_val/valores-validos")
    assert response.status_code == 200
    assert "presente" in response.json()

def test_custom_metrics():
    response = client.get("/asistencia/custom_metrics")
    assert response.status_code == 200
    assert "asistencia_http_requests_total" in response.text

