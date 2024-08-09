from pydantic import BaseModel
from typing import Optional
from .menu_items import MenuItem
from .resources import Resource

class RecipeBase(BaseModel):
    menu_item_id: int
    resource_id: int
    amount: float

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(BaseModel):
    menu_item_id: Optional[int] = None
    resource_id: Optional[int] = None
    amount: Optional[float] = None

class Recipe(RecipeBase):
    id: int
    resource_id: int
    menu_item_id: int

    resources: Resource = None
    menu_item: MenuItem = None

    class ConfigDict:
        from_attributes = True