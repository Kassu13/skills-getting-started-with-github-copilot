import copy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_global


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Snapshot and restore the in-memory activities before/after each test."""
    original = copy.deepcopy(activities_global)
    try:
        yield
    finally:
        activities_global.clear()
        activities_global.update(copy.deepcopy(original))
