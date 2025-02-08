from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional
from sqlalchemy.orm import Session

T = TypeVar("T")

class AbstractRepository(ABC, Generic[T]):

    def __init__(self, session: Session, model: T):
        self.session: Session = session
        self.model: T = model

    @abstractmethod
    def get_by_identifier(self, id) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def add(self, entity: T) -> None:
        pass

    @abstractmethod
    def delete(self, identifier) -> None:
        pass