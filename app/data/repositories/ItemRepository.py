from contextlib import AbstractContextManager
from typing import Callable, Iterator
from sqlalchemy.orm import Session
from app.models.entities.Item import Item


class ItemRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Item]:
        with self.session_factory() as session:
            return session.query(Item).all()

    def get(self, entity_id: int) -> Item:
        with self.session_factory() as session:
            entity = session.query(Item).filter(Item.id == entity_id).first()
            if not entity:
                raise ItemNotFoundError(entity_id)
            return entity

    def add(self, entity) -> Item:
        item = Item(id=entity.id, name=entity.name, description=entity.description)
        with self.session_factory() as session:
            session.add(item)
            session.commit()
            session.refresh(item)
            return item

    def delete_by_id(self, entity_id: int) -> None:
        with self.session_factory() as session:
            entity: Item = session.query(Item).filter(Item.id == entity_id).first()
            if not entity:
                raise ItemNotFoundError(entity_id)
            session.delete(entity)
            session.commit()


class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class ItemNotFoundError(NotFoundError):

    entity_name: str = "Item"
