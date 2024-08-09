from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models


def create(db: Session, customers):
    db_customers = models.Customer(
        name=customers.name,
        phone_number=customers.phone_number,
        email=customers.email,
        address=customers.address
    )
    db.add(db_customers)
    db.commit()
    db.refresh(db_customers)
    
    return db_customers


def read_all(db: Session):
    return db.query(models.Customer).all()


def read_one(db: Session, customers_id):
    return db.query(models.Customer).filter(models.Customer.id == customers_id).first()


def update(db: Session, customers_id, customers):
    db_customers = db.query(models.Customer).filter(models.Customer.id == customers_id)
    update_data = customers.model_dump(exclude_unset=True)
    db_customers.update(update_data, synchronize_session=False)
    db.commit()
    
    return db_customers.first()


def delete(db: Session, customers_id):
    db_customers = db.query(models.Customer).filter(models.Customer.id == customers_id)
    db_customers.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
