from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models


def create(db: Session, order):
    db_order = models.Order(
        customer_name=order.customer_name,
        order_date=order.order_date,
        tracking_num=order.tracking_num,
        order_status=order.order_status,
        price=order.price,
        description=order.description,
        takeout=order.takeout
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    return db_order


def read_all(db: Session):
    return db.query(models.Order).all()


def read_one(db: Session, order_id):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def update(db: Session, order_id, order):
    db_order = db.query(models.Order).filter(models.Order.id == order_id)
    update_data = order.model_dump(exclude_unset=True)
    db_order.update(update_data, synchronize_session=False)
    db.commit()

    return db_order.first()


def delete(db: Session, order_id):
    db_order = db.query(models.Order).filter(models.Order.id == order_id)
    db_order.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
