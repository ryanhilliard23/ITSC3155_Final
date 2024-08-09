from pydantic import BaseModel
from typing import Optional

class ResourceBase(BaseModel):
    item: str
    amount: int

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[int] = None

class Resource(ResourceBase):
    id: int

    class ConfigDict:
        from_attributes = True
