from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .customers import Customer

class PaymentBase(BaseModel):
    card_number: str
    expiration_date: datetime
    customers_id: int
    transaction_status: str

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(PaymentBase):
    card_number: Optional[str] = None
    expiration_date: Optional[datetime] = None
    customers_id: Optional[int] = None
    transaction_status: Optional[str] = None

class Payment(PaymentBase):
    id: int
    customers_id: int
    customers: Customer = None

    class ConfigDict:
        from_attributes = True
