from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import resource_management as schemas
from ..controllers import resource_management as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Resource Management'],
    prefix="/resource_management"
)

@router.post("/", response_model=schemas.ResourceManagement)
def create(resource_management: schemas.ResourceManagementCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, resource_management=resource_management)

@router.get("/", response_model=List[schemas.ResourceManagement])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{resource_management_id}", response_model=schemas.ResourceManagement)
def read_one(resource_management_id: int, db: Session = Depends(get_db)):
    resource_management = controller.read_one(db, resource_management_id=resource_management_id)
    if resource_management is None:
        raise HTTPException(status_code=404, detail="Resource Management not found")
    return resource_management

@router.put("/{resource_management_id}", response_model=schemas.ResourceManagement)
def update(resource_management_id: int, resource_management: schemas.ResourceManagementUpdate, db: Session = Depends(get_db)):
    db_resource_management = controller.read_one(db, resource_management_id=resource_management_id)
    if db_resource_management is None:
        raise HTTPException(status_code=404, detail="Resource Management not found")
    return controller.update(db=db, resource_management_id=resource_management_id, resource_management=resource_management)

@router.delete("/{resource_management_id}")
def delete(resource_management_id: int, db: Session = Depends(get_db)):
    db_resource_management = controller.read_one(db, resource_management_id=resource_management_id)
    if db_resource_management is None:
        raise HTTPException(status_code=404, detail="Resource Management not found")
    return controller.delete(db=db, resource_management_id=resource_management_id)