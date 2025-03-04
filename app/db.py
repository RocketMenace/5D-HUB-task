from typing import Annotated, Any

from fastapi import Depends

from app import main
from app.config import config

DATABASE_URL = (
    f"mongodb://{config.DATABASE_URL}:{config.DATABASE_PORT}/{config.DB_NAME}"
)


def get_db_session():
    return main.app.database


SessionDep = Annotated[Any, Depends(get_db_session)]
