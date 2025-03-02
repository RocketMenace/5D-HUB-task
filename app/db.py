from app.config import config

DATABASE_URL = f"mongodb://{config.DATABASE_URL}:{config.DATABASE_PORT}/{config.DB_NAME}"


