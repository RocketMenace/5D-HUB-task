from fastapi import FastAPI
from app.router import router

app = FastAPI(title="5D HUB training task")

app.include_router(router, prefix="")