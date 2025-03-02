from pydantic import BaseModel, ConfigDict


class URLBase(BaseModel):
    pass


class URLIn(URLBase):
    target_url: str


class URL(URLBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    shortened_url: str
