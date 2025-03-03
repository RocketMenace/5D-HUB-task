from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse
from app.schemas import URLIn, URL
from app.services import create, get_url
from app.db import SessionDep

router = APIRouter()


@router.post(path="", status_code=status.HTTP_201_CREATED, response_model=URL, response_model_by_alias=False)
async def post_link(url: URLIn, session: SessionDep):
    return await create(url, session)


@router.get(path="/{shorten_url_id}", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def get_link(shorten_url_id: str, session: SessionDep):
    link = await get_url(shorten_url_id, session)
    return RedirectResponse(link)