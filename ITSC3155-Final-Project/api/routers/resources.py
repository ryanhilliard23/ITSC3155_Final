from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import resources as schemas
from ..controllers import resources as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Resource'],
    prefix="/resource"
)

@router.post("/", response_model=schemas.Resource)
def create(resources: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, resources=resources)

@router.get("/", response_model=List[schemas.Resource])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{resources_id}", response_model=schemas.Resource)
def read_one(resources_id: int, db: Session = Depends(get_db)):
    resources = controller.read_one(db, resources_id=resources_id)
    if resources is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources

@router.put("/{resources_id}", response_model=schemas.Resource)
def update(resources_id: int, resources: schemas.ResourceBase, db: Session = Depends(get_db)):
    db_resource = controller.read_one(db, resources_id=resources_id)
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return controller.update(db=db, resources_id=resources_id, resources=resources)

@router.delete("/{resources_id}")
def delete(resources_id: int, db: Session = Depends(get_db)):
    db_resource = controller.read_one(db, resources_id=resources_id)
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return controller.delete(db=db, resources_id=resources_id)
