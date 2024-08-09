from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status, Response, Depends
from ..models import models


def create(db: Session, promotion):
    db_promotion = models.Promotion(
        name=promotion.name,
        expiration_date=promotion.expiration_date,
        promo_code=promotion.promo_code  
    )
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
   
    return db_promotion

def update(db: Session, promotion_id, promotion):
    db_promotions = db.query(models.Promotion).filter(models.Promotion.id == promotion_id)
    update_data = promotion.dict(exclude_unset=True)
    db_promotions.update(update_data, synchronize_session=False)
    db.commit()
    
    return db_promotions.first()

def read_all(db: Session):
    return db.query(models.Promotion).all()

def read_one(db: Session, promotion_id):
    return db.query(models.Promotion).filter(models.Promotion.id == promotion_id).first()

def delete(db: Session, promotion_id):
    db_promotions = db.query(models.Promotion).filter(models.Promotion.id == promotion_id)
    db_promotions.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
