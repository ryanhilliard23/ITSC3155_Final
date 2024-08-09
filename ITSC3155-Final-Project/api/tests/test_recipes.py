from fastapi.testclient import TestClient
from ..controllers import recipes as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_recipe(db_session):
    #Sample Data
    recipe_data = {
        "menu_item_id": "1",
        "resource_id": "2",
        "amount": "25"
    }

    recipe_object = model.Recipe(**recipe_data)

    #Call create function
    created_info = controller.create(db_session, recipe_object)

    #Test Cases
    assert created_info is not None
    assert created_info.menu_item_id == "1"
    assert created_info.resource_id == "2"
    assert created_info.amount == "25"

