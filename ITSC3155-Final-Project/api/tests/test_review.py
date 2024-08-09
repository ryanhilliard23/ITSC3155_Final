from fastapi.testclient import TestClient
from ..controllers import review as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_review(db_session):
    #Sample Data
    rating_data = {
        "review": "Great",
        "rating": "10"
    }

    review_object = model.Review(**rating_data)

    #Call create function
    created_info = controller.create(db_session, review_object)

    #Test Cases
    assert created_info is not None
    assert created_info.review == "Great"
    assert created_info.rating == "10"

