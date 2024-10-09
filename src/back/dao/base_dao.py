from typing import TypeVar, Any, Optional
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")
SchemaType = TypeVar("SchemaType")

class BaseDAO:
    MODEL = None

    @classmethod
    def _create(cls, db: Session, obj_in: SchemaType) -> ModelType:
        db_obj = cls.MODEL(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @classmethod
    def read_by_id(cls, db: Session, id: int) -> Optional[ModelType]:
        return db.query(cls.MODEL).get(id)

    @classmethod
    def _read_by(cls, db: Session, **filters: Any) -> ModelType:
        return db.query(cls.MODEL).filter_by(**filters).first()

    @classmethod
    def _update(cls, db: Session, db_obj: ModelType, obj_in: SchemaType) -> ModelType:
        obj_data = obj_in.dict(exclude_unset=True)  # Only update provided fields
        for field in obj_data:
            setattr(db_obj, field, obj_data[field])
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @classmethod
    def _delete(cls, db: Session, db_obj: ModelType) -> None:
        db.delete(db_obj)
        db.commit()
