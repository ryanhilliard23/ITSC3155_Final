from fastapi.testclient import TestClient
from ..controllers import customers as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_customer(db_session):
    #Sample Data
    customer_data = {
        "name": "John Doe",
        "phone_number": "0123456789",
        "email": "johndoe@gmail.com",
        "address": "John Doe Road"
    }

    customer_object = model.Customer(**customer_data)

    #Call create function
    created_info = controller.create(db_session, customer_object)

    #Test Cases
    assert created_info is not None
    assert created_info.name == "John Doe"
    assert created_info.email == "johndoe@gmail.com"
    assert created_info.phone_number == "0123456789"
    assert created_info.address == "John Doe Road"


