from pydantic import BaseModel
from typing import Optional
from .menu_items import MenuItem
from .promotion import Promotion
from .orders import Order

class OrderDetailBase(BaseModel):
    quantity: int
    price: float
    order_id: int
    item_id: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailUpdate(BaseModel):
    quantity: Optional[int] = None
    price: Optional[float] = None
    order_id: Optional[int] = None
    item_id: Optional[int] = None
    

class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    item_id: int

    order: Order = None
    menu_item: MenuItem = None
    promo: Optional[Promotion] = None

    class ConfigDict:
        from_attributes = True
