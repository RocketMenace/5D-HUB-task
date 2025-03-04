from pydantic import BaseModel, ConfigDict, Field


class URLBase(BaseModel):
    pass


class URLIn(URLBase):
    long_url: str


class URL(URLBase):
    model_config = ConfigDict(
        from_attributes=True, populate_by_name=True, arbitrary_types_allowed=True
    )
    short_url: str
    long_url: str
