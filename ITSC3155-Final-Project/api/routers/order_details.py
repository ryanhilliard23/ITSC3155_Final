from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import order_details as schemas
from ..controllers import order_details as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['OrderDetail'],
    prefix="/order_details"
)

@router.post("/", response_model=schemas.OrderDetail)
def create(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, order_details=order_detail)

@router.get("/", response_model=List[schemas.OrderDetail])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{order_detail_id}", response_model=schemas.OrderDetail)
def read_one(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = controller.read_one(db, order_details_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return order_detail

@router.put("/{order_detail_id}", response_model=schemas.OrderDetail)
def update(order_detail_id: int, order_detail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    db_order_detail = controller.read_one(db, order_details_id=order_detail_id)
    if db_order_detail is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return controller.update(db=db, order_details_id=order_detail_id, order_details=order_detail)

@router.delete("/{order_detail_id}")
def delete(order_detail_id: int, db: Session = Depends(get_db)):
    db_order_detail = controller.read_one(db, order_details_id=order_detail_id)
    if db_order_detail is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return controller.delete(db=db, order_details_id=order_detail_id)
