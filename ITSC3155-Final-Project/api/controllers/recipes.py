from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models

def create(db: Session, recipes):
    db_recipes = models.Recipe(
        menu_item_id=recipes.menu_item_id,
        resource_id=recipes.resource_id,
        amount=recipes.amount
    )
    db.add(db_recipes)
    db.commit()
    db.refresh(db_recipes)
    
    return db_recipes

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, recipes_id):
    return db.query(models.Recipe).filter(models.Recipe.id == recipes_id).first()

def update(db: Session, recipes_id, recipes):
    db_recipes = db.query(models.Recipe).filter(models.Recipe.id == recipes_id)
    update_data = recipes.model_dump(exclude_unset=True)
    db_recipes.update(update_data, synchronize_session=False)
    db.commit()

    return db_recipes.first()

def delete(db: Session, recipes_id):
    db_recipes = db.query(models.Recipe).filter(models.Recipe.id == recipes_id)
    db_recipes.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
