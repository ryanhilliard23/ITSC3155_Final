from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import review as schemas
from ..controllers import review as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Review'],
    prefix="/Review"
)

@router.post("/", response_model=schemas.Review)
def create(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, review=review)

@router.get("/", response_model=List[schemas.Review])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{review_id}", response_model=schemas.Review)
def read_one(review_id: int, db: Session = Depends(get_db)):
    review = controller.read_one(db, review_id=review_id)
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@router.put("/{review_id}", response_model=schemas.Review)
def update(review_id: int, review: schemas.ReviewBase, db: Session = Depends(get_db)):
    db_review = controller.read_one(db, review_id=review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return controller.update(db=db, review_id=review_id, review=review)

@router.delete("/{review_id}")
def delete(review_id: int, db: Session = Depends(get_db)):
    db_review = controller.read_one(db, review_id=review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return controller.delete(db=db, review_id=review_id)