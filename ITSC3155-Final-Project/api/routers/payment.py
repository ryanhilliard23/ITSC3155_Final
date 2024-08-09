from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..schemas import payment as schemas
from ..dependencies.database import get_db
from ..controllers import payment as controller

router = APIRouter(
    tags=['Payment'],
    prefix="/payments"
)

@router.post("/", response_model=schemas.Payment)
def create(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, payment=payment)

@router.get("/", response_model=list[schemas.Payment])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{payment_id}", response_model=schemas.Payment)
def read_one(payment_id: int, db: Session = Depends(get_db)):
    info = controller.read_one(db, payment_id=payment_id)
    if info is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return info

@router.put("/{payment_id}", response_model=schemas.Payment)
def update(payment_id: int, payment_update: schemas.PaymentUpdate, db: Session = Depends(get_db)):
    payment_db = controller.read_one(db, payment_id=payment_id)
    if payment_db is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return controller.update(db=db, payment_id=payment_id, payment=payment_update)

@router.delete("/{payment_id}")
def delete(payment_id: int, db: Session = Depends(get_db)):
    info = controller.read_one(db, payment_id=payment_id)
    if info is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return controller.delete(db=db, payment_id=payment_id)