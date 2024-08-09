from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import menu_items as schemas
from ..controllers import menu_items as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['MenuItem'],
    prefix="/menu_items"
)

@router.post("/", response_model=schemas.MenuItem)
def create(menu_item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, menu_items=menu_item)

@router.get("/", response_model=List[schemas.MenuItem])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{menu_items_id}", response_model=schemas.MenuItem)
def read_one(menu_item_id: int, db: Session = Depends(get_db)):
    menu_item = controller.read_one(db, menu_items_id=menu_item_id)
    if menu_item is None:
        raise HTTPException(status_code=404, detail="Menu Item not found")
    return menu_item

@router.put("/{menu_items_id}", response_model=schemas.MenuItem)
def update(menu_item_id: int, menu_item: schemas.MenuItemBase, db: Session = Depends(get_db)):
    db_menu_item = controller.read_one(db, menu_items_id=menu_item_id)
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="Menu Item not found")
    return controller.update(db=db, menu_items_id=menu_item_id, menu_items=menu_item)

@router.delete("/{menu_items_id}")
def delete(menu_item_id: int, db: Session = Depends(get_db)):
    db_menu_item = controller.read_one(db, menu_items_id=menu_item_id)
    if db_menu_item is None:
        raise HTTPException(status_code=404, detail="Menu Item not found")
    return controller.delete(db=db, menu_items_id=menu_item_id)
