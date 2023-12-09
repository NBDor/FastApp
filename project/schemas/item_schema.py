from models import Item
from pydantic import (
    BaseModel,
    ConfigDict,
)
from typing import (
    Optional
)

class ItemBase(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    tax: Optional[float]

class ItemInDB(ItemBase):
    id: int
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    tax: Optional[float]

    model_config = ConfigDict(from_attributes=True)