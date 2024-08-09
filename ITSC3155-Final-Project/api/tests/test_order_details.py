from fastapi.testclient import TestClient
from ..controllers import order_details as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order_details(db_session):
    #Sample Data
    order_details_data = {
        "quantity": "5",
        "price": "10",
        "order_id": "1",
        "item_id": "1"
    }

    order_details_object = model.OrderDetail(**order_details_data)

    #Call create function
    created_info = controller.create(db_session, order_details_object)

    #Test Cases
    assert created_info is not None
    assert created_info.quantity == "5"
    assert created_info.price == "10"
    assert created_info.order_id == "1"
    assert created_info.item_id == "1"

