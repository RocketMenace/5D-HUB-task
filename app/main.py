from fastapi import FastAPI
from app.router import router

app = FastAPI(title="5D HUB training task", root_path="api/")

app.include_router(router, prefix="urls")