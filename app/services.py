from hashlib import md5
from typing import Any

from app.db import SessionDep
from app.schemas import URLIn


async def create(url: URLIn, database: SessionDep) -> dict[str, Any]:
    data = {"long_url": url.long_url}
    short_url = md5(url.long_url.encode()).hexdigest()[:7]
    data["short_url"] = short_url
    new_url = await database["urls"].insert_one(data)
    return await database["urls"].find_one({"_id": new_url.inserted_id})


async def get_url(shorten_url_id: str, database: SessionDep) -> str:
    url = await database["urls"].find_one({"short_url": {"$eq": shorten_url_id}})
    return url["long_url"]
