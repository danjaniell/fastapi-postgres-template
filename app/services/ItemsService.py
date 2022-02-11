from typing import Iterator
from app.data.repositories import ItemRepository
from app.models.entities.Item import Item


class ItemService:
    def __init__(self, item_repository: ItemRepository) -> None:
        self._repository: ItemRepository = item_repository

    def get_items(self) -> Iterator[Item]:
        return self._repository.get_all()

    def get_item_by_id(self, id: int) -> Item:
        return self._repository.get(id)

    def add_item(self, item) -> Item:
        return self._repository.add(item)

    def delete_item_by_id(self, id: int) -> None:
        return self._repository.delete_by_id(id)
