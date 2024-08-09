from fastapi.testclient import TestClient
from ..controllers import payment as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_payment(db_session):
    #Sample Data
    payment_data = {
        "card_number": "1111222233334444",
        "expiration_date": "0820225",
        "customers_id": "1",
        "transaction_status": "Approved"
    }

    payment_object = model.Payment(**payment_data)

    #Call create function
    created_info = controller.create(db_session, payment_object)

    #Test Cases
    assert created_info is not None
    assert created_info.card_number == "1111222233334444"
    assert created_info.expiration_date == "0820225"
    assert created_info.customers_id == "1"
    assert created_info.transaction_status == "Approved"

