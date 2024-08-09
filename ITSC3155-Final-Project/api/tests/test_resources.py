from fastapi.testclient import TestClient
from ..controllers import resources as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_resource(db_session):
    #Sample Data
    resource_data = {
        "item": "Cheese",
        "amount": "25"
    }

    resource_object = model.Resource(**resource_data)

    #Call create function
    created_info = controller.create(db_session, resource_object)

    #Test Cases
    assert created_info is not None
    assert created_info.item == "Cheese"
    assert created_info.amount == "25"

