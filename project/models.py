from database import Base as BaseDBModel
from sqlalchemy import Integer, String, DateTime, Float, func
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from datetime import datetime

class Base(BaseDBModel):
    abstract = True


class Item(Base):
    __tablename__ = "item"

    id = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    tax: Mapped[float] = mapped_column(Float)
    creation_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        insert_default=func.now(),
        default=None,
    )
    last_modified: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        insert_default=func.now(),
        default=None,
        onupdate=func.now(),
    )