from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderBase(BaseModel):
    customer_name: str
    order_date: datetime
    tracking_num: int
    order_status: str
    price: float
    description: str
    takeout: bool

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    order_date: Optional[datetime] = None
    tracking_num: Optional[int] = None
    order_status: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    takeout: Optional[bool] = None

class Order(OrderBase):
    id: int

    class ConfigDict:
        from_attributes = True
