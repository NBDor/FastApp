from config.settings import app_settings
from models import Base
from sqlalchemy.orm import Session
from typing import Any, List, Optional

class BaseCrud:
    def __init__(self, current_model: Base) -> None:
        self.model = current_model
        self.page_size = app_settings.PAGE_SIZE

    def get_model_instance(self, db: Session, model_id: int, **kwargs: Any) -> Optional[Base]:
        return db.query(self.model).filter(self.model.id == model_id).filter_by(**kwargs).first()
    
    def get_model_instances_list(
            self,
            db: Session,
            skip: int = 0,
            limit: int = app_settings.PAGE_SIZE,
            **kwargs: Any
    ) -> List[Base]:
        return db.query(self.model).filter_by(**kwargs).offset(skip).limit(limit).all()

    def create_model_instance(self, db: Session,craete_schema) -> Base:
        db_instance = self.model(**craete_schema.model_dump(exclude_unset=True))
        db.add(db_instance)
        db.commit()
        db.refresh(db_instance)
        return db_instance
    
    def update_model_instance(self, db: Session, instance_id: int, update_schema) -> Base:
        db_instance = self.get_model_instance(db, instance_id)
        if db_instance:
            update_data = update_schema.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_instance, key, value)
            db.commit()
            db.refresh(db_instance)
        return db_instance
    
    def delete_model_instance(self, db: Session, instance_id: int) -> Base:
        db_instance = self.get_model_instance(db, instance_id)
        if db_instance:
            db.delete(db_instance)
            db.commit()
            db.refresh(db_instance)
        return db_instance
