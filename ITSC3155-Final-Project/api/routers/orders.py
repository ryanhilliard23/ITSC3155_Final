from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import orders as schemas
from ..controllers import orders as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Order'],
    prefix="/orders"
)

@router.post("/", response_model=schemas.Order)
def create(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, order=order)

@router.get("/", response_model=List[schemas.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{order_id}", response_model=schemas.Order)
def read_one(order_id: int, db: Session = Depends(get_db)):
    order = controller.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=schemas.Order)
def update(order_id: int, order: schemas.OrderBase, db: Session = Depends(get_db)):
    db_order = controller.read_one(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return controller.update(db=db, order_id=order_id, order=order)

@router.delete("/{order_id}")
def delete(order_id: int, db: Session = Depends(get_db)):
    db_order = controller.read_one(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return controller.delete(db=db, order_id=order_id)
