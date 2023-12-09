from database import get_db
from fastapi import APIRouter, Depends, status
from models import Item as DBModel
from crud.item_crud import ItemCrud
from schemas.item_schema import ItemInDB


router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)
item_crud = ItemCrud(DBModel)
ITEM_NOT_FOUND = "Item not found"


@router.get("/", response_model=list[ItemInDB], status_code=status.HTTP_200_OK)
def get_items_endpoint(
    skip: int = 0,
    limit: int = 100,
    db=Depends(get_db),
):
    return item_crud.get_model_instances_list(skip=skip, limit=limit, db=db)