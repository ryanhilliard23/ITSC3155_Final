from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models

def create(db: Session, resource_management):
    db_resource_management = models.ResourceManagement(
        ingredient_name=resource_management.ingredient_name, 
        amount=resource_management.amount,
        unit = resource_management.unit
    )
    db.add(db_resource_management)
    db.commit()
    db.refresh(db_resource_management)

    return db_resource_management

def read_all(db: Session):
    return db.query(models.ResourceManagement).all()

def read_one(db: Session, resource_management_id):
    return db.query(models.ResourceManagement).filter(models.ResourceManagement.id == resource_management_id).first()

def update(db: Session, resource_management_id, resource_management):
    db_resource_management = db.query(models.ResourceManagement).filter(models.ResourceManagement.id == resource_management_id)
    update_data = resource_management.model_dump(exclude_unset=True)
    db_resource_management.update(update_data, synchronize_session=False)
    db.commit()

    return db_resource_management.first()

def delete(db: Session, resource_management_id):
    db_resource_management = db.query(models.ResourceManagement).filter(models.ResourceManagement.id == resource_management_id)
    db_resource_management.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)