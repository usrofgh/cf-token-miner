from typing import TypeVar, Any, Optional, List
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")
SchemaType = TypeVar("SchemaType")

class BaseDAO:
    MODEL = None

    @classmethod
    def create(cls, db: Session, obj_in: SchemaType) -> ModelType:
        """
        Create a db record and returns it
        :param db:
        :param obj_in:
        :return:
        """
        db_obj = cls.MODEL(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @classmethod
    def read_by_id(cls, db: Session, id: int) -> Optional[ModelType]:
        """
        Retrieve one entry by PK
        :param db:
        :param id:
        :return:
        """
        return db.query(cls.MODEL).get(id)

    @classmethod
    def read_by_email(cls, db: Session, email: str) -> Optional[ModelType]:
        """
        Retrieve one entry by Email
        :param db:
        :param email:
        :return:
        """
        return db.query(cls.MODEL).get(email)

    @classmethod
    def read_all(cls, db: Session, **filters: Any) -> List[ModelType]:
        """
        Retrieve all entries
        :param db:
        :param filters: any fields of an entry
        :return:
        """
        return db.query(cls.MODEL).filter_by(**filters).all()

    @classmethod
    def update(cls, db: Session, db_obj: ModelType, obj_in: SchemaType) -> ModelType:
        """
        Update an existing entry
        :param db:
        :param db_obj:
        :param obj_in:
        :return:
        """
        obj_data = obj_in.dict(exclude_unset=True)  # Only update provided fields
        for field in obj_data:
            setattr(db_obj, field, obj_data[field])
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @classmethod
    def delete(cls, db: Session, id: int) -> bool:
        """
        Delete an entry by ID
        :param db:
        :param id:
        :return:
        """
        db_obj = db.query(cls.MODEL).get(id)
        if db_obj:
            db.delete(db_obj)
            db.commit()
            return True
        return False
