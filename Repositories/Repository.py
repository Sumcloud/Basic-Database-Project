from sqlalchemy.orm import Session
from typing import Type, List, Optional
from Repositories.AbstractRepository import AbstractRepository

T = AbstractRepository.__parameters__[0]

class Repository(AbstractRepository[T]):
    def __init__(self, session: Session, model: Type[T]): # type: ignore
        super().__init__(session, model)

    def get_by_identifier(self, id) -> Optional[T]: # type: ignore
        return self.session.query(self.model).filter_by(id=id).first()

    def get_all(self) -> List[T]: # type: ignore
        return self.session.query(self.model).all()

    def add(self, entity: T) -> None: # type: ignore
        self.session.add(entity)
        self.session.commit()

    def delete(self, id) -> None:
        obj = self.get_by_identifier(id)
        if obj:
            self.session.delete(obj)
            self.session.commit()
