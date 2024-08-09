from pydantic import BaseModel
from typing import Optional

class ResourceManagementBase(BaseModel):
    ingredient_name: str
    amount: int
    unit: str

class ResourceManagementCreate(ResourceManagementBase):
    pass

class ResourceManagementUpdate(BaseModel):
    ingredient_name: Optional[str] = None
    amount: Optional[int] = None
    unit: Optional[str] = None

class ResourceManagement(ResourceManagementBase):
    id: int

    class ConfigDict:
        from_attributes = True