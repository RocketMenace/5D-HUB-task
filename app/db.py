from app.config import config
from app import main
from fastapi import Depends
from typing import Annotated, Any

DATABASE_URL = (
    f"mongodb://{config.DATABASE_URL}:{config.DATABASE_PORT}/{config.DB_NAME}"
)


def get_db_session():
    return main.app.database


SessionDep = Annotated[Any, Depends(get_db_session)]
