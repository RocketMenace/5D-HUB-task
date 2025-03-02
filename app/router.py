from fastapi import APIRouter, status
from app.schemas import URLIn, URL
from app.services import create, get_link

router = APIRouter()


@router.post(path="", status_code=status.HTTP_201_CREATED, response_model=URL)
async def post_link(url: URLIn):
    return await create(url)


@router.get(path="/{shorten_url_id}", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def get_link(shorten_url_id: int):
    return await get_link(shorten_url_id)
