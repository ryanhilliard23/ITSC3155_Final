from fastapi.testclient import TestClient
from ..controllers import promotion as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_promotion(db_session):
    #Sample Data
    promotion_data = {
        "name": "8/24 Promotion",
        "expiration_date": "2024-08-24",
        "promo_code": "AUG24",
    }

    promotion_object = model.Promotion(**promotion_data)

    #Call create function
    created_info = controller.create(db_session, promotion_object)

    #Test Cases
    assert created_info is not None
    assert created_info.name == "8/24 Promotion"
    assert created_info.expiration_date == "2024-08-24"
    assert created_info.promo_code == "AUG24"


