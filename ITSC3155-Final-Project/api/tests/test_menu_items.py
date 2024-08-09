from fastapi.testclient import TestClient
from ..controllers import menu_items as controller
from ..main import app
import pytest
from ..models import models as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_menu_items(db_session):
    #Sample Data
    menu_items_data = {
        "name": "Burger",
        "price": "10",
        "ingredients": "Beef, Lettuce, Tomato",
        "food_category": "Main Course",
        "calories": "500"
    }

    menu_items_object = model.MenuItem(**menu_items_data)

    #Call create function
    created_info = controller.create(db_session, menu_items_object)

    #Test Cases
    assert created_info is not None
    assert created_info.name == "Burger"
    assert created_info.price == "10"
    assert created_info.ingredients == "Beef, Lettuce, Tomato"
    assert created_info.food_category == "Main Course"
    assert created_info.calories == "500"

