from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    phone_number: str
    email: str
    address: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

class Customer(CustomerBase):
    id: int

    class ConfigDict:
        from_attributes = True