from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    #Sample Data
    order_data = {
        "customer_name": "John Doe",
        "description": "This is a test",
        "order_date": "2024-08-02",
        "order_status": "In Progress",
        "price": 10.00,
        "takeout": False
    }

    order_object = model.Order(**order_data)

    #Call create function
    created_info = controller.create(db_session, order_object)

    #Test Cases
    assert created_info is not None
    assert created_info.customer_name == "John Doe"
    assert created_info.description == "This is a test"
    assert created_info.order_date == "2024-08-02"
    assert created_info.order_status == "In Progress"
    assert created_info.price == 10.00
    assert created_info.takeout == False