from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models


def create(db: Session, payment):
    db_payment = models.Payment(
        customers_id=payment.customers_id,
        card_number=payment.card_number,
        expiration_date=payment.expiration_date,
        transaction_status=payment.transaction_status
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)

    return db_payment


def read_all(db: Session):
    return db.query(models.Payment).all()


def read_one(db: Session, payment_id):
    return db.query(models.Payment).filter(models.Payment.id == payment_id).first()


def update(db: Session, payment_id, payment):
    db_payment = db.query(models.Payment).filter(models.Payment.id == payment_id)
    update_data = payment.model_dump(exclude_unset=True)
    db_payment.update(update_data, synchronize_session=False)
    db.commit()
    
    return db_payment.first()


def delete(db: Session, payment_id):
    db_payment = db.query(models.Payment).filter(models.Payment.id == payment_id)
    db_payment.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
