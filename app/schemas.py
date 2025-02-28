from pydantic import BaseModel, ConfigDict

class URLBase(BaseModel):
    pass

class URLIn(URLBase):
    pass

class URL(URLBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    pass