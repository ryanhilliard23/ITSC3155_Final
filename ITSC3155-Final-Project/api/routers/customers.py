from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..schemas import customers as schemas
from ..dependencies.database import get_db
from ..controllers import customers as controller

router = APIRouter(
    tags=['Customer'],
    prefix="/customers"
)

@router.post("/", response_model=schemas.Customer)
def create(customers: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, customers=customers)

@router.get("/", response_model=list[schemas.Customer])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{customers_id}", response_model=schemas.Customer)
def read_one(customers_id: int, db: Session = Depends(get_db)):
    info = controller.read_one(db, customers_id=customers_id)
    if info is None:
        raise HTTPException(status_code=404, detail="User not found")
    return info

@router.put("/{customers_id}", response_model=schemas.Customer)
def update(customers_id: int, customers_update: schemas.CustomerUpdate, db: Session = Depends(get_db)):
    customers_db = controller.read_one(db, customers_id=customers_id)
    if customers_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return controller.update(db=db, customers_id=customers_id, customers=customers_update)

@router.delete("/{customers_id}")
def delete(customers_id: int, db: Session = Depends(get_db)):
    info = controller.read_one(db, customers_id=customers_id)
    if info is None:
        raise HTTPException(status_code=404, detail="User not found")
    return controller.delete(db=db, customers_id=customers_id)
