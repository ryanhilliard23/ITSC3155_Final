from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models


def create(db: Session, menu_items):
    db_menu_items = models.MenuItem(
        name=menu_items.name,
        price=menu_items.price,
        ingredients=menu_items.ingredients,
        food_category=menu_items.food_category,
        calories=menu_items.calories
    )
    db.add(db_menu_items)
    db.commit()
    db.refresh(db_menu_items)
    
    return db_menu_items


def read_all(db: Session):
    return db.query(models.MenuItem).all()


def read_one(db: Session, menu_items_id):
    return db.query(models.MenuItem).filter(models.MenuItem.id == menu_items_id).first()


def update(db: Session, menu_items_id, menu_items):
    db_menu_items = db.query(models.MenuItem).filter(models.MenuItem.id == menu_items_id)
    update_data = menu_items.model_dump(exclude_unset=True)
    db_menu_items.update(update_data, synchronize_session=False)
    db.commit()
    
    return db_menu_items.first()


def delete(db: Session, menu_items_id):
    db_menu_items = db.query(models.MenuItem).filter(models.MenuItem.id == menu_items_id)
    db_menu_items.delete(synchronize_session=False)
    db.commit()
   
    return Response(status_code=status.HTTP_204_NO_CONTENT)
