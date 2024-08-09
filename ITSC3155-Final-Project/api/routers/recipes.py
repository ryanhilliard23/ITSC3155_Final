from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..schemas import recipes as schemas
from ..controllers import recipes as controller
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/Recipes",
    tags=["Recipes"],
)

@router.post("/", response_model=schemas.Recipe)
def create(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, recipes=recipe)

@router.get("/", response_model=List[schemas.Recipe])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{recipe_id}", response_model=schemas.Recipe)
def read_one(recipe_id: int, db: Session = Depends(get_db)):
    recipe = controller.read_one(db=db, recipes_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.put("/{recipe_id}", response_model=schemas.Recipe)
def update(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    existing_recipe = controller.read_one(db=db, recipes_id=recipe_id)
    if existing_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return controller.update(db=db, recipes_id=recipe_id, recipes=recipe)

@router.delete("/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(recipe_id: int, db: Session = Depends(get_db)):
    existing_recipe = controller.read_one(db=db, recipes_id=recipe_id)
    if existing_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return controller.delete(db=db, recipes_id=recipe_id)
