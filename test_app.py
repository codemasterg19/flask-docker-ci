import pytest
from app import app


def test_home_route():
    """Verifica que la ruta '/' responde con código 200."""
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
