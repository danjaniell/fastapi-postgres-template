from pydantic import BaseModel


class ItemRequest(BaseModel):
    id: int
    name: str
    description: str
