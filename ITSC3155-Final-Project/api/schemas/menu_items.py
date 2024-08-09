from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    name: str
    price: float
    ingredients: str
    food_category: str
    calories: Optional[int] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(MenuItemBase):
    name: Optional[str] = None
    price: Optional[float] = None
    ingredients: Optional[str] = None
    food_category: Optional[str] = None
    calories: Optional[int] = None

class MenuItem(MenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True
