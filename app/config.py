from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )


class GlobalConfig(BaseSettings):
    DATABASE_URL: str
    DATABASE_PORT: str
    DB_FORCE_ROLL_BACK: bool = False


class DevConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix="DEV_", env_file=".env", env_file_encoding="utf-8", extra="allow")
    DATABASE_URL: str
    DATABASE_PORT: str
    DB_NAME: str

class TestConfig(GlobalConfig):
    DB_FORCE_ROLL_BACK: bool = True


def get_config(config: str):
    configs = {"dev": DevConfig, "test": TestConfig}
    return configs[config]()


config = get_config("dev")
