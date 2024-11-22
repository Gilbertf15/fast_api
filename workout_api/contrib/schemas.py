

from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributos =True
