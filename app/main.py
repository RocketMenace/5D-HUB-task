from contextlib import asynccontextmanager

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.db import DATABASE_URL
from app.router import router


@asynccontextmanager
async def db_lifespan(application: FastAPI):
    application.mongo_db_client = AsyncIOMotorClient(DATABASE_URL)
    application.database = application.mongo_db_client.get_default_database()
    ping_response = await application.database.command("ping")
    if int(ping_response["ok"]) != 1:
        raise Exception("Problem connecting to database cluster.")
    yield
    application.mongo_db_client.close()


app = FastAPI(lifespan=db_lifespan, title="5D HUB training task", root_path="/api")

app.include_router(router, prefix="/urls")
