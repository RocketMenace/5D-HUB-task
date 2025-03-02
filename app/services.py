from app.schemas import URLIn
from typing import Any
from hashlib import md5


async def create(url: URLIn) -> str:
    return md5(url.target_url.encode()).hexdigest()[:7]


async def get_link(shorten_url_id: int) -> str:
    pass
