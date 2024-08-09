from pydantic import BaseModel
from typing import Optional

class PromotionBase(BaseModel):
    name: str
    expiration_date: str
    promo_code: str

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    name: Optional[str] = None
    expiration_date: Optional[str] = None
    promo_code: Optional[str] = None

class Promotion(PromotionBase):
    id: int
    promo_code: str

    class ConfigDict:
        from_attributes = True
