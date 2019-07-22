import pytest
from src.app import app

@pytest.fixture
def client():
    return app.test_client()
