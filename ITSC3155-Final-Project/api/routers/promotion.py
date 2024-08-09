from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import promotion as schemas
from ..controllers import promotion as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Promotion'],
    prefix="/promotion"
)


@router.post("/", response_model=schemas.Promotion)
def create(promotion: schemas.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, promotion=promotion)

@router.get("/", response_model=List[schemas.Promotion])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{promotion_id}", response_model=schemas.Promotion)
def read_one(promotion_id: int, db: Session = Depends(get_db)):
    promotion = controller.read_one(db, promotion_id=promotion_id)
    if promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion

@router.put("/{promotion_id}", response_model=schemas.Promotion)
def update(promotion_id: int, promotion: schemas.PromotionUpdate, db: Session = Depends(get_db)):
    db_promotion = controller.read_one(db, promotion_id=promotion_id)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return controller.update(db=db, promotion_id=promotion_id, promotion=promotion)

@router.delete("/{promotion_id}")
def delete(promotion_id: int, db: Session = Depends(get_db)):
    db_promotion = controller.read_one(db, promotion_id=promotion_id)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return controller.delete(db=db, promotion_id=promotion_id)