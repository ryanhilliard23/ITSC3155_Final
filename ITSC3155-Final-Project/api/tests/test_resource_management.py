from fastapi.testclient import TestClient
from ..controllers import resource_management as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_resource_management(db_session):
    #Sample Data
    resource_management_data = {
        "ingredient_name": "Cheese",
        "amount": "25",
        "unit": "lbs",
    }

    resource_object = model.ResourceManagement(**resource_management_data)

    #Call create function
    created_info = controller.create(db_session, resource_object)

    #Test Cases
    assert created_info is not None
    assert created_info.ingredient_name == "Cheese"
    assert created_info.amount == "25"
    assert created_info.unit == "lbs"

