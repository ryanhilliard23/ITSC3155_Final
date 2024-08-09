from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    review: str
    rating: int

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    review: Optional[str] = None
    rating: Optional[int] = None

class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True
