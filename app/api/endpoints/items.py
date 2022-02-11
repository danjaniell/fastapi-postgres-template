from app.services.ItemsService import ItemService
from app.core.containers import Container
from app.data.repositories.ItemRepository import NotFoundError
from app.models.requests.ItemRequest import ItemRequest
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Response, status

router = APIRouter()


@router.get("/all")
@inject
async def get_all(
    item_service: ItemService = Depends(Provide[Container.item_service]),
):
    return item_service.get_items()


@router.get("/get/{id}")
@inject
async def get(
    id: int,
    item_service: ItemService = Depends(Provide[Container.item_service]),
):
    try:
        return item_service.get_item_by_id(id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/add", status_code=status.HTTP_201_CREATED)
@inject
async def add(
    request: ItemRequest,
    item_service: ItemService = Depends(Provide[Container.item_service]),
):
    return item_service.add_item(request)


@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete(
    id: int,
    item_service: ItemService = Depends(Provide[Container.item_service]),
):
    try:
        item_service.delete_item_by_id(id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/status")
async def get_status():
    return {"status": "OK"}
