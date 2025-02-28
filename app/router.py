from fastapi import APIRouter, status

router = APIRouter()

@router.post(path="", status_code=status.HTTP_201_CREATED)
async def post_link():
    pass

@router.get(path="", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def get_link(url_id: int):
    pass